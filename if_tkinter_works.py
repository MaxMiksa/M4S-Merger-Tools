#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 tkinter 是否正常工作
Test if tkinter is working correctly
"""

import sys
import traceback

print("=" * 60)
print("测试 tkinter 功能")
print("Testing tkinter Functionality")
print("=" * 60)
print()

try:
    print("[1] 导入 tkinter... / Importing tkinter...")
    import tkinter as tk
    from tkinter import messagebox
    print("[1] ✓ tkinter 导入成功 / tkinter imported successfully")
except Exception as e:
    print(f"[1] ✗ tkinter 导入失败 / Failed to import tkinter: {e}")
    traceback.print_exc()
    sys.exit(1)

try:
    print("[2] 创建根窗口... / Creating root window...")
    root = tk.Tk()
    print("[2] ✓ 根窗口创建成功 / Root window created successfully")
except Exception as e:
    print(f"[2] ✗ 根窗口创建失败 / Failed to create root window: {e}")
    traceback.print_exc()
    sys.exit(1)

try:
    print("[3] 设置窗口属性... / Setting window properties...")
    root.title("测试窗口 / Test Window")
    root.geometry("500x300") # 稍微调大一点以容纳双语文字
    print("[3] ✓ 窗口属性设置成功 / Window properties set successfully")
except Exception as e:
    print(f"[3] ✗ 窗口属性设置失败 / Failed to set window properties: {e}")
    traceback.print_exc()
    root.destroy()
    sys.exit(1)

try:
    print("[4] 添加标签... / Adding label...")
    label_text = "如果看到这个窗口，说明 tkinter 正常工作！\nIf you see this window, tkinter is working correctly!"
    label = tk.Label(root, text=label_text, font=("Arial", 12))
    label.pack(pady=50)
    print("[4] ✓ 标签添加成功 / Label added successfully")
except Exception as e:
    print(f"[4] ✗ 标签添加失败 / Failed to add label: {e}")
    traceback.print_exc()
    root.destroy()
    sys.exit(1)

try:
    print("[5] 更新窗口... / Updating window...")
    root.update_idletasks()
    root.update()
    print("[5] ✓ 窗口更新成功 / Window updated successfully")
except Exception as e:
    print(f"[5] ✗ 窗口更新失败 / Failed to update window: {e}")
    traceback.print_exc()
    root.destroy()
    sys.exit(1)

print()
print("[6] 窗口应该已经显示，请检查是否有窗口弹出")
print("[6] The window should be visible now, please check for popups")
print("[6] 5秒后自动关闭窗口... / Closing window automatically in 5 seconds...")
print()

try:
    # 5秒后自动关闭
    def close_window():
        print("[7] 关闭窗口... / Closing window...")
        root.quit()
        root.destroy()
        print("[7] ✓ 窗口已关闭 / Window closed")
    
    root.after(5000, close_window)
    
    print("[6] 启动事件循环... / Starting event loop...")
    root.mainloop()
    print("[6] ✓ 事件循环已退出 / Event loop exited")
except Exception as e:
    print(f"[6] ✗ 事件循环失败 / Event loop failed: {e}")
    traceback.print_exc()
    try:
        root.destroy()
    except:
        pass
    sys.exit(1)

print()
print("=" * 60)
print("测试完成！如果看到窗口，说明 tkinter 正常工作")
print("Test completed! If you saw the window, tkinter is working correctly.")
print("=" * 60)