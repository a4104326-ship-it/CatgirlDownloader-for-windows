@echo off
setlocal
cd /d "%~dp0"

if not exist "C:\msys64\ucrt64\bin\python.exe" (
    echo MSYS2 UCRT64 nao encontrado em C:\msys64\ucrt64\bin\python.exe
    echo Instale o MSYS2 e os pacotes necessarios descritos no README.
    pause
    exit /b 1
)

set PYTHONPATH=%cd%
"C:\msys64\ucrt64\bin\python.exe" -m src.main