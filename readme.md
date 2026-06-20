# 视频解析下载 APK

基于 Python + yt-dlp + Kivy 的跨平台视频解析下载应用。

## 功能特性

- **自动识别链接**：从分享文本中自动提取视频链接
- **多平台支持**：抖音、快手、小红书、B站、视频号、YouTube、TikTok 等
- **一键解析下载**：粘贴链接即可解析并下载
- **离线使用**：完全独立运行，无需外部服务
- **进度显示**：实时显示下载进度

## 使用方法

1. **复制分享文本**（例如抖音分享）：
   ```
   0.23 复制打开抖音，看看【幸运女神☘️的作品】第1集|和这样的丈夫一起生活，女人太可怜了# 电视... https://v.douyin.com/avZuoAu-LEc/ 01/27 L@w.sE :7pm CUL:/
   ```

2. **打开 APK**，粘贴到输入框

3. **点击"提取链接"**，自动识别出视频链接

4. **点击"解析"**，开始下载视频

## 安装方式

### 方式一：直接下载 APK（推荐）

从 [GitHub Releases](https://github.com/your-repo/releases) 下载最新 APK 文件安装。

### 方式二：使用 GitHub Actions 自动打包

1. **Fork 本仓库**

2. **启用 GitHub Actions**
   - 进入仓库 Settings → Actions → General
   - 选择 "Allow all actions and reusable workflows"

3. **触发打包**
   - 推送代码到 main 分支
   - 或创建新 tag（如 `v1.0.0`）
   - 或手动点击 Actions → Build Android APK → Run workflow

4. **下载 APK**
   - 打包完成后，在 Actions 页面下载 artifact
   - 或查看 Releases 页面（如果创建了 tag）

### 方式三：本地打包（需要 Linux 环境）

```bash
pip install buildozer cython
cd video-parser-mobile
buildozer android debug
```

APK 位置：`bin/video-parser-mobile-1.0.0-debug.apk`

## 支持的平台

| 平台 | 状态 | 备注 |
|------|------|------|
| 抖音 | ✅ 支持 | 短链接自动展开 |
| 快手 | ✅ 支持 | |
| 小红书 | ✅ 支持 | |
| B站 | ✅ 支持 | |
| 视频号 | ⚠️ 部分支持 | 可能需要 Cookie |
| YouTube | ✅ 支持 | |
| TikTok | ✅ 支持 | |
| 百家号 | ✅ 支持 | |

## 注意事项

- APK 体积较大（约 100-150MB），因为包含 Python 运行时和 yt-dlp
- 部分平台（如微信视频号）可能需要登录 Cookie 才能解析
- 建议在 Wi-Fi 环境下下载视频
- 下载的视频仅供个人学习使用，请尊重版权

## 技术栈

- **Kivy**：跨平台 Python GUI
- **yt-dlp**：视频解析核心
- **Buildozer**：Android 打包工具

## 项目结构

```
video-parser-mobile/
├── main.py              # Kivy 主程序
├── video_parser.py      # 视频解析核心
├── buildozer.spec       # Android 打包配置
├── requirements.txt     # Python 依赖
└── README.md           # 说明文档
```

## 常见问题

### Q: 为什么有些视频无法解析？
A: 部分平台有反爬保护，可能需要 Cookie 或特定 Headers。建议在设置中添加对应平台的 Cookie。

### Q: 下载的视频保存在哪里？
A: 默认保存在 `Downloads/VideoParser` 目录。

### Q: 如何添加 Cookie？
A: 在设置界面中添加对应平台的 Cookie（JSON 格式）。

## 许可证

MIT License
