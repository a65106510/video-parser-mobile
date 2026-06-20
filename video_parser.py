import re
import os
import json
import tempfile
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    yt_dlp = None


class VideoParser:
    """视频解析核心"""

    def __init__(self, output_dir=None):
        if output_dir:
            self.output_dir = Path(output_dir)
        else:
            # 默认保存到 Downloads/VideoParser
            if os.name == 'nt':  # Windows
                self.output_dir = Path(os.environ.get('USERPROFILE', '.')) / 'Downloads' / 'VideoParser'
            else:  # Linux/Mac/Android
                self.output_dir = Path.home() / 'Downloads' / 'VideoParser'

        self.output_dir.mkdir(parents=True, exist_ok=True)

    def extract_url_from_text(self, text):
        """从分享文本中提取链接"""
        # 匹配 http/https 链接
        url_pattern = r'https?://[^\s]+'
        matches = re.findall(url_pattern, text)
        if matches:
            return matches[0]

        # 匹配短链接（如 v.douyin.com/xxx）
        short_pattern = r'v\.douyin\.com/[a-zA-Z0-9_-]+'
        matches = re.findall(short_pattern, text)
        if matches:
            return f"https://{matches[0]}"

        return None

    def identify_platform(self, url):
        """识别视频平台"""
        platforms = [
            ("抖音", r"(?:https?://)?(?:www\.)?douyin\.com|v\.douyin\.com"),
            ("快手", r"(?:https?://)?(?:www\.)?kuaishou\.com"),
            ("小红书", r"(?:https?://)?(?:www\.)?xiaohongshu\.com|xhslink\.com"),
            ("B站", r"(?:https?://)?(?:www\.)?bilibili\.com"),
            ("视频号", r"(?:https?://)?channels\.weixin\.qq\.com"),
            ("YouTube", r"(?:https?://)?(?:www\.)?youtube\.com"),
            ("TikTok", r"(?:https?://)?(?:www\.)?tiktok\.com"),
            ("百家号", r"(?:https?://)?baijiahao\.baidu\.com"),
        ]
        for name, pattern in platforms:
            if re.search(pattern, url):
                return name
        return "未知平台"

    def parse_and_download(self, url, progress_callback=None):
        """解析并下载视频"""
        if yt_dlp is None:
            return {"success": False, "error": "yt-dlp 未安装"}

        # 识别平台
        platform = self.identify_platform(url)

        # 配置 yt-dlp
        ydl_opts = {
            'outtmpl': str(self.output_dir / '%(title)s.%(ext)s'),
            'no-playlist': True,
            'quiet': True,
            'no_warnings': True,
        }

        # 添加进度回调
        if progress_callback:
            def _progress(d):
                if d['status'] == 'downloading':
                    total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
                    downloaded = d.get('downloaded_bytes', 0)
                    if total > 0:
                        percent = (downloaded / total) * 100
                        progress_callback(percent, f"下载中... {percent:.1f}%")
                elif d['status'] == 'finished':
                    progress_callback(100, "下载完成")

            ydl_opts['progress_hooks'] = [_progress]

        try:
            if progress_callback:
                progress_callback(0, f"正在解析 [{platform}]...")

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)

            filepath = ydl.prepare_filename(info)
            if not Path(filepath).exists():
                # 尝试查找下载的文件
                ext = info.get('ext', 'mp4')
                title = info.get('title', 'video')
                safe_title = self.sanitize_filename(title)
                candidates = list(self.output_dir.glob(f"{safe_title}*.{ext}"))
                if candidates:
                    filepath = str(candidates[0])
                else:
                    filepath = str(self.output_dir / f"{safe_title}.{ext}")

            return {
                "success": True,
                "filepath": filepath,
                "filename": os.path.basename(filepath),
                "title": info.get('title', ''),
                "platform": platform,
                "duration": info.get('duration', 0),
                "thumbnail": info.get('thumbnail', ''),
            }

        except Exception as e:
            return {"success": False, "error": str(e)}

    def sanitize_filename(self, name):
        """清理文件名中的非法字符"""
        name = re.sub(r'[\\/:*?"<>|]', '_', name)
        return name.strip()[:100]

    def get_downloaded_videos(self):
        """获取已下载的视频列表"""
        videos = []
        for f in self.output_dir.glob('*.mp4'):
            videos.append({
                'filename': f.name,
                'path': str(f),
                'size': f.stat().st_size,
                'modified': f.stat().st_mtime,
            })
        return sorted(videos, key=lambda x: x['modified'], reverse=True)
