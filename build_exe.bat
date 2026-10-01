@echo off
cd /d "%~dp0"
py -m pip install pyinstaller pycaw comtypes
pyinstaller --onefile --windowed --name VolumeBooster volume_booster.py
echo El ejecutable esta en la carpeta dist.
pause
