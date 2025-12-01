# M4S Merger Tools v1.1.0 | [中文说明](https://github.com/MaxMiksa/M4S-Merger-Tools/blob/main/README.md)

A desktop application for Windows that uses a user-friendly Graphical Interface (GUI) to seamlessly merge M4S video and audio fragments and finalize the muxing process into a single file.  
Specifically designed for processing M4S files (commonly found in video/audio downloads from Bilibili/B站).

<img src="presentation/Presentation%20video%20-%20M4S%20Merger%20Tools%20v1.0.0.gif" 
     alt="M4S Merger Tools Demonstration GIF" 
     width="1000"/>
[Watch a clearer video demonstration](https://github.com/MaxMiksa/M4S-Merger-Tools/blob/main/presentation/Presentation%20video%20-%20M4S%20Merger%20Tools%20v1.0.0.MP4)

## Features

*   🎬 **Video Merging**: Merges multiple M4S video fragments ➡️ into a single video file.
*   🎵 **Audio Merging**: Merges multiple M4S audio fragments ➡️ into a single audio file.
*   🎞️ **Audio/Video Muxing**: Combines merged M4S video and audio files ➡️ into a complete MP4 file (with both picture and sound).
*   🚀 **One-Click Automation**: A fully automated workflow, covering environment setup (FFmpeg installation), error handling, merging, and final muxing.
*   💻 **Graphical User Interface (GUI)**: Eliminates the hassle of CMD command-line usage. Simple, click-and-use operation.
*   🌐 **Customizable Interface** 🎨: Supports switching between **Chinese** and **English**, and features **Light/Dark** display modes.
*   📝 **Real-Time Logging**: Displays processing progress and detailed log information.
*   ⚙️ **Automatic FFmpeg Installation**: Automatically detects and installs FFmpeg on first run (supports custom download and installation paths).
*   🛡️ **Robust Error Handling**: Provides detailed error prompts at every stage, helping users quickly identify and resolve issues.

## System Requirements

-   **If using the EXE file**: Windows 10 / 11
-   **If running from source code**: Python 3.7 or higher

## Installation

### Recommended: Use the Compiled EXE File (Download and Run)

1.  Download the `M4S Merger Tools.exe` from the `Release` section on the right side of this page.
2.  Run `M4S Merger Tools.exe`.
    *   **Note**: A network connection is required for the first run (to automatically download FFmpeg).

<details>
<summary> Alternative: Running from Source Code </summary>

#### 1. Install Python

If you haven't installed Python yet, please download and install it from the [Official Python Website](https://www.python.org/downloads/).

#### 2. Run the Program

1.  Download or clone this project.
2.  Double-click `start.bat`.

</details>

### Automatic FFmpeg Setup (If Needed)

**On first run**, if the program detects that FFmpeg is not installed, the installation dialog will automatically pop up:

1.  Select the FFmpeg installation directory (default is the `ffmpeg` folder under the user's home directory).
2.  Click the "Install" button.
3.  The program will automatically:
    -   **Download** FFmpeg (approx. 100MB, takes about 10 seconds).
    -   **Extract** it to the specified directory.
    -   **Add** the FFmpeg executable path to the system's PATH environment variable.
4.  After installation is complete, **restart the application** to begin using it.

<details>
<summary> Alternative: Detailed Manual FFmpeg Installation </summary>
1. Download the Windows version of FFmpeg from the [FFmpeg official website](https://ffmpeg.org/download.html).
2. Unzip it to any directory (e.g., `C:\ffmpeg`).
3. Add FFmpeg's `bin` directory to the system PATH environment variable:
   - Right-click "This PC" → "Properties" → "Advanced system settings" → "Environment Variables".
   - Find `Path` in "System variables" and click "Edit".
   - Add the path to the FFmpeg `bin` directory (e.g., `C:\ffmpeg\bin`).
   - Click "OK" to save.
</details>

## Usage

### Basic Workflow

1.  **Select Video File(s)**: Click "Select Video File(s)" button and choose the M4S video fragments to be merged.
2.  **Select Audio File(s)**: Click "Select Audio File(s)" button and choose the M4S audio fragments to be merged.
3.  **Select Output Directory**: Click "Select Output Directory" button to choose where the resulting file should be saved.
4.  **Execute Processing**:
    -   **Merge Video**: Merges video fragments only.
    -   **Merge Audio**: Merges audio fragments only.
    -   **One-Click Processing**: Automatically completes video merging, audio merging, and final audio/video muxing (**Recommended**).

### Output File Descriptions

-   `merged_video.mp4`: The resulting merged video file.
-   `merged_audio.mp4`: The resulting merged audio file.
-   `final_output.mp4`: The complete, final video file after muxing (generated when using "One-Click Processing").

## Important Notes

1.  **File Order**: Merging is performed based on the sequence in which the files were selected in the file dialog. Please ensure the order is correct.
2.  **File Format**: Currently, M4S format is primarily supported. Other formats might work but have not been extensively tested.
3.  **FFmpeg Path**: If FFmpeg is not detected in the system PATH, you can modify the `ffmpeg_path` parameter in the source code.
4.  **Processing Time**: Large files may require significant processing time; please be patient.
5.  **Network Connection**: Required on the first run for FFmpeg download.

## Advanced & Troubleshooting

<details>
<summary>Package to Executable (If running from source code, not using the downloaded EXE file)</summary>

The program provides three ways to package the application into a standalone `.exe` file, which can be run without installing Python.

### Method 1: Use the Batch Script (Recommended)

1.  Double-click and run `build_exe.bat`.
2.  The script will automatically install PyInstaller (if not present) and start the packaging process.
3.  The executable file will be located in `dist\M4S Merger Tools v1.x.0.exe`.

### Method 2: Use the Python Script

```bash
python build_exe.py
```

### Method 3: Manual Packaging

```bash
# Install PyInstaller
pip install pyinstaller

# Package using the batch script
build_exe.bat

# Or use PyInstaller directly
pyinstaller --onefile --windowed --name "M4S Merger Tools v1.x.0" main.py
```

### Distribution Notes

The packaged `.exe` file can be:
- Copied and run directly on any Windows PC.
- Shared via USB drives or cloud storage.
- On its first run, it will automatically detect and install FFmpeg if needed (requires a network connection).

</details>

<details>
<summary>Robust Error Prompts and Handling Mechanism</summary>

The program features a comprehensive error handling system, displaying detailed error messages at every stage.

### Startup Stage Checks
- Python version check
- Module import check
- GUI initialization check
   
### Runtime Stage Checks
- File selection error prompts
- FFmpeg invocation error prompts
- File processing error prompts
- Network connection error prompts (during FFmpeg download)
   
### Installation Stage Checks
- FFmpeg download error prompts
- Extraction error prompts
- PATH environment variable modification error prompts
   
**If the program fails to respond**:
1. Check if an error prompt window has popped up (it might be hidden behind other windows).
2. Check the Task Manager to see if a process is running.
3. Try running the application with administrator privileges.
4. Check the program log output (if running from source code).

</details>

<details>
<summary>Frequently Asked Questions (FAQ)</summary>

### Q: Why does it prompt "FFmpeg not found"?

A: The program automatically checks for FFmpeg on first run. If it's not installed, the installation dialog will appear—follow the prompts. If you have installed it manually but the program still can't detect it, please ensure FFmpeg has been correctly added to the system PATH environment variable and restart the application.

### Q: What if FFmpeg installation fails?

A: Possible reasons:
- **Network connection issues**: Please check your internet connection.
- **Insufficient disk space**: FFmpeg requires approximately 200MB of space.
- **Permission issues**: Ensure you have write permission for the installation directory.

If the automatic installation fails, you can install FFmpeg manually (refer to the "Manual FFmpeg Installation" details in the Installation section).

### Q: The program is unresponsive when I launch it?

A: Please check the following:
1. Is there an error prompt window hidden behind other windows?
2. Is a process running in the Task Manager?
3. Try running the program with administrator privileges.
4. If using the EXE file, ensure the file is complete and not blocked by antivirus software.

### Q: The merged video has no sound?

A: Please ensure that you have selected **both** the video file(s) and the audio file(s), and then use the **"One-Click Processing"** function for muxing.

### Q: What if processing fails?

A: Check the error message in the log output area. Common causes include:
- File paths containing special characters.
- Corrupted M4S file fragments.
- Insufficient disk space.
- FFmpeg version incompatibility.
- Network connection issues (during FFmpeg download).

</details>

<details>
<summary>Technical Specifications</summary>
   
- **GUI Framework**: Python tkinter
- **Video Processing Engine**: FFmpeg
- **Error Handling**: Comprehensive exception capturing and user notification mechanisms

</details>

<details>
<summary>License</summary>

This project is licensed under the MIT License.

</details>

## Contribution and Contact

Welcome to submit Issues and Pull Requests!  
Any questions or suggestions? Please contact Max Kong (Carnegie Mellon University, Pittsburgh, PA).

Max Kong: kongzheyuan@outlook.com | zheyuank@andrew.cmu.edu