#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
M4S 文件处理工具 - 主程序入口
M4S File Processing Tool - Main Program Entry
"""

import sys
import os
import traceback
from pathlib import Path

def show_error(title, message):
    """显示错误消息框 / Show error message box"""
    try:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口 / Hide main window
        messagebox.showerror(title, message)
        root.destroy()
    except:
        # 如果 tkinter 也无法使用，尝试使用 Windows 消息框
        # If tkinter fails, try using Windows message box
        try:
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, message, title, 0x10)  # MB_ICONERROR
        except:
            print(f"错误 / Error: {title}\n{message}")
            input("按回车键退出 / Press Enter to exit...")

def main():
    """主函数，包含错误处理 / Main function with error handling"""
    try:
        print("[启动/Init] 开始初始化程序... / Starting initialization...")
        
        # 检查 Python 版本
        print(f"[检查/Check] Python 版本 / Version: {sys.version}")
        if sys.version_info < (3, 7):
            error_msg = (
                f"需要 Python 3.7 或更高版本\n"
                f"Python 3.7 or higher is required\n\n"
                f"当前版本 / Current version: {sys.version}"
            )
            print(f"[错误/Error] {error_msg.replace(chr(10), ' ')}") # Replace newline with space for log
            show_error("版本错误 / Version Error", error_msg)
            return
        
        print("[检查/Check] Python 版本检查通过 / Python version check passed")
        
        # 导入 GUI 模块
        print("[导入/Import] 正在导入 GUI 模块... / Importing GUI module...")
        try:
            from gui import M4SProcessorApp
            print("[导入/Import] GUI 模块导入成功 / GUI module imported successfully")
        except ImportError as e:
            error_msg = (
                f"无法导入 GUI 模块\n"
                f"Failed to import GUI module\n\n"
                f"错误 / Error: {str(e)}\n\n"
                f"请确保所有文件都在同一目录下\n"
                f"Please ensure all files are in the same directory."
            )
            print(f"[错误/Error] {error_msg.replace(chr(10), ' ')}")
            print(f"[调试/Debug] 当前目录 / Current Directory: {os.getcwd()}")
            print(f"[调试/Debug] 文件列表 / File List: {os.listdir('.')}")
            show_error("导入错误 / Import Error", error_msg)
            return
        except Exception as e:
            error_msg = (
                f"初始化 GUI 模块时出错\n"
                f"Error initializing GUI module\n\n"
                f"错误 / Error: {str(e)}\n\n"
                f"详细信息 / Details:\n{traceback.format_exc()}"
            )
            print(f"[错误/Error] {error_msg.replace(chr(10), ' ')}")
            show_error("初始化错误 / Initialization Error", error_msg)
            return
        
        # 创建并运行应用
        print("[启动/Startup] 正在创建应用程序... / Creating application...")
        try:
            app = M4SProcessorApp()
            print("[启动/Startup] 应用程序创建成功 / Application created successfully")
            print("[启动/Startup] 检查窗口状态... / Checking window state...")
            print(f"[启动/Startup] 窗口可见性 / Window visibility: {app.root.winfo_viewable()}")
            print(f"[启动/Startup] 窗口状态 / Window state: {app.root.state()}")
            print("[启动/Startup] 正在启动 GUI 事件循环... / Starting GUI event loop...")
            print("[启动/Startup] 注意: mainloop() 会阻塞，直到窗口关闭 / Note: mainloop() blocks until window closes")
            app.run()
            print("[退出/Exit] 程序正常退出 / Program exited normally")
        except Exception as e:
            error_msg = (
                f"程序运行时出错\n"
                f"Runtime Error\n\n"
                f"错误 / Error: {str(e)}\n\n"
                f"详细信息 / Details:\n{traceback.format_exc()}"
            )
            print(f"[错误/Error] {error_msg.replace(chr(10), ' ')}")
            show_error("运行时错误 / Runtime Error", error_msg)
            return
            
    except Exception as e:
        # 捕获所有未处理的异常
        error_msg = (
            f"程序启动失败\n"
            f"Program startup failed\n\n"
            f"错误 / Error: {str(e)}\n\n"
            f"详细信息 / Details:\n{traceback.format_exc()}"
        )
        print(f"[严重错误/Critical] {error_msg.replace(chr(10), ' ')}")
        show_error("启动错误 / Startup Error", error_msg)

if __name__ == "__main__":
    main()