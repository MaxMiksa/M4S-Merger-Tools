@echo off
chcp 65001 >nul
echo ========================================================
echo M4S 文件处理工具 - 启动脚本
echo M4S File Processing Tool - Launcher Script
echo ========================================================
echo.
echo 正在启动程序...
echo Starting the program...
echo.

REM 检查 Python 是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未找到 Python！
    echo [Error] Python not found!
    echo.
    echo 请确保已安装 Python 3.7 或更高版本
    echo Please ensure Python 3.7 or higher is installed.
    echo.
    pause
    exit /b 1
)

REM 检查 main.py 是否存在
if not exist main.py (
    echo [错误] 未找到 main.py 文件！
    echo [Error] 'main.py' file not found!
    echo.
    echo 请确保在正确的目录下运行此脚本
    echo Please ensure you are running this script in the correct directory.
    echo.
    pause
    exit /b 1
)

REM 检查必要的模块文件
if not exist gui.py (
    echo [错误] 未找到 gui.py 文件！
    echo [Error] 'gui.py' file not found!
    echo.
    echo 请确保所有文件都在同一目录下
    echo Please ensure all files are in the same directory.
    echo.
    pause
    exit /b 1
)

if not exist m4s_processor.py (
    echo [错误] 未找到 m4s_processor.py 文件！
    echo [Error] 'm4s_processor.py' file not found!
    echo.
    echo 请确保所有文件都在同一目录下
    echo Please ensure all files are in the same directory.
    echo.
    pause
    exit /b 1
)

if not exist ffmpeg_installer.py (
    echo [错误] 未找到 ffmpeg_installer.py 文件！
    echo [Error] 'ffmpeg_installer.py' file not found!
    echo.
    echo 请确保所有文件都在同一目录下
    echo Please ensure all files are in the same directory.
    echo.
    pause
    exit /b 1
)

echo [信息] 文件检查通过
echo [Info] File check passed.
echo [信息] 正在启动程序...
echo [Info] Launching application...
echo.
echo ========================================================
echo 程序输出（调试信息）
echo Program Output (Debug Info)
echo ========================================================
echo.

REM 运行程序并捕获输出
python main.py

REM 检查退出代码
if errorlevel 1 (
    echo.
    echo ========================================================
    echo [错误] 程序运行失败（退出代码: %errorlevel%）
    echo [Error] Program execution failed (Exit Code: %errorlevel%)
    echo ========================================================
    echo.
    echo 可能的原因 / Possible causes:
    echo 1. Python 版本不兼容（需要 3.7 或更高版本）
    echo    Incompatible Python version (Requires 3.7 or higher)
    echo 2. 缺少必要的 Python 模块
    echo    Missing necessary Python modules
    echo 3. 程序运行时出错
    echo    Runtime error
    echo.
    echo 请查看上方的错误信息以获取更多详情
    echo Please check the error messages above for more details.
    echo.
    pause
    exit /b 1
) else (
    REM 正常退出，等待一下让用户看到
    echo.
    echo [信息] 程序已正常退出
    echo [Info] Program exited normally.
    timeout /t 2 >nul
)