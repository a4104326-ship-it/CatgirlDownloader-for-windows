# CatgirlDownloader for Windows

Experimental Windows port of NyarchLinux/CatgirlDownloader.

## Status
This fork runs on Windows using MSYS2 UCRT64 with GTK4/libadwaita.

It is not a native standalone .exe yet.

## Run on Windows
1. Install MSYS2
2. Install the required UCRT64 packages
3. Double-click `run-catgirldownloader-windows.bat`

## Notes
This fork currently uses Windows-specific adjustments for:
- Python module naming conflicts
- loading .ui files from disk
- loading app icons from local icon paths

## Help wanted
Contributions are welcome for:
- portable packaging
- PyInstaller support
- native Windows .exe packaging
# I didn't know exactly what I was doing!
Everything was done using Perplexity (to understand what to do and in what order), Windows Notepad, msys2, and hope.
