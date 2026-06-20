        if yt_dlp is None:
            # 尝试再次安装
            try:
                import subprocess, sys
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'yt-dlp', '--quiet'])
                import yt_dlp
            except Exception:
                return {"success": False, "error": "yt-dlp 安装失败，请检查网络连接"}