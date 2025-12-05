# Version 1.3.0

## ✨ 启动更快，混流更爽

**软件一打开就能看到界面，混流速度回到几秒内，深色主题的按钮也看得见、点得准。**

| 类别 | 详细内容 |
| --- | --- |
| 启动体验 | 不再卡在 `ffmpeg -version`，窗口即刻出现，日志提示“正在检查 FFmpeg”。 |
| 初始化提示 | 按钮会弹出 “FFmpeg 正在初始化…” 的提醒，避免误触。 |
| 混流速度 | 采用 `-c copy`，95MB + 34MB 的文件几秒内完成混流。 |
| 深色按键 | “选择文件”“更改路径”“仅合并视频/音频”等按钮统一底色和悬停反馈。 |

## ✨ Faster launch, snappier muxing

**The window shows up right away, muxing finishes in seconds, and dark-mode buttons share a clear palette with hover feedback.**

| Category | Details |
| --- | --- |
| Launch | No more waiting for `ffmpeg -version`; the UI renders instantly and logs “Checking FFmpeg…”. |
| Guard | Buttons warn “FFmpeg is initializing…” if setup is still running. |
| Mux speed | Using stream copy keeps muxing a 95MB + 34MB pair within a couple of seconds. |
| Dark theme | “Select Files”, “Change Path”, and merge buttons reuse the same secondary colors and hover states. |

---

# Version 1.2.0

## ✨ 命名更清晰，默认更贴心

**输出文件带时间戳、桌面默认路径自动生效，中间文件只在临时目录出现。**

| 类别 | 详细内容 |
| --- | --- |
| 输出命名 | 文件自动追加 “YYYY-MM-DD_HH-MM-SS”，不会再被覆盖。 |
| 中间文件 | 单文件直接复用，多文件只在临时目录合并后立刻删除。 |
| 默认路径 | 没选目录会自动保存到 Desktop。 |
| 文档同步 | README 中英双语补充命名示例和桌面默认说明。 |

## ✨ Clearer filenames and smarter defaults

**Every export is timestamped, temps live only in a cleanup folder, and Desktop is the default save location.**

| Category | Details |
| --- | --- |
| Naming | `Merged_*` / `Muxed_*_YYYY-MM-DD_HH-MM-SS.mp4` prevents overwrites. |
| Temp handling | Single streams reuse originals; multi-part merges run inside `TemporaryDirectory()`. |
| Default path | Falls back to Desktop whenever the user skips choosing a folder. |
| Docs | Both README files describe the naming rule and Desktop default. |

---

# Version 1.1.0

## ✨ 全新界面，双语提示

**界面完全翻新，支持中英切换、双语日志，还能一键切换亮/暗模式。**

| 类别 | 详细内容 |
| --- | --- |
| UI/UX | 卡片式布局、圆角控件和新字体让操作更舒服。 |
| 多语言 | 按钮、提示、日志、安装向导都能即时中英切换。 |
| 主题模式 | 一键切换浅色 / 深色，适配不同环境。 |
| 安装流程 | FFmpeg 安装器提供双语说明和进度提示。 |

## ✨ Major UI overhaul with bilingual support

**A modern card-style UI plus real-time Chinese/English switching make the tool friendlier and clearer.**

| Category | Details |
| --- | --- |
| Interface | Rounded cards, consistent spacing, and modern typography. |
| Languages | Buttons, logs, and pop-ups switch languages instantly. |
| Themes | Light/Dark toggle adapts to any lighting conditions. |
| Installer | Bilingual FFmpeg setup dialog with progress feedback. |

---

# Version 1.0.0

## ✨ 桌面版首次发布

**第一次亮相就提供视频/音频合并、混流、一键处理和自动安装 FFmpeg。**

| 类别 | 详细内容 |
| --- | --- |
| 合并功能 | `.m4s` 片段按选中顺序合并成完整视频或音频。 |
| 混流 | 把音轨和画面打包成带声 MP4。 |
| GUI | `customtkinter` 界面提供文件列表、日志和提示。 |
| FFmpeg | 首次运行自动下载、解压并配置 PATH。 |

## ✨ First desktop release

**Delivers video/audio merging, muxing, a GUI, and automatic FFmpeg setup right from day one.**

| Category | Details |
| --- | --- |
| Merging | Combine multiple `.m4s` segments following the user’s order. |
| Muxing | Produce a single MP4 with both audio and video streams. |
| GUI | Visual interface built with `customtkinter`, including logs and dialogs. |
| FFmpeg | Detects and installs FFmpeg automatically when missing. |
