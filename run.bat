@echo off
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
  echo Python no esta instalado o esta bloqueado en este ordenador.
  pause
  exit /b 1
)
py -m pip install -r requirements.txt
py volume_booster.py
