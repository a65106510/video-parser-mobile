@echo off
chcp 65001 >nul
echo ==========================================
echo   一键推送到 GitHub 并触发 APK 打包
echo ==========================================
echo.

cd /d F:\红果搬运\video-parser-mobile

echo [1/3] 推送代码到 main 分支...
git push origin main
if %errorlevel% neq 0 (
    echo 推送 main 分支失败，请检查网络
    pause
    exit /b 1
)

echo.
echo [2/3] 创建标签 v1.0.1...
git tag v1.0.1 -f
if %errorlevel% neq 0 (
    echo 创建标签失败
    pause
    exit /b 1
)

echo.
echo [3/3] 推送标签触发 GitHub Actions...
git push origin v1.0.1 -f
if %errorlevel% neq 0 (
    echo 推送标签失败，请检查网络
    pause
    exit /b 1
)

echo.
echo 推送成功！
echo 请打开 https://github.com/a65106510/video-parser-mobile/actions 查看打包进度
pause
