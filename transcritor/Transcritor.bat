@echo off
chcp 65001 >nul
title Transcritor de video
cd /d "%~dp0"

if exist "ambiente\Scripts\pythonw.exe" (
  start "" "ambiente\Scripts\pythonw.exe" transcrever.py --janela
  exit /b 0
)
if exist "python-portatil\pythonw.exe" (
  "python-portatil\python.exe" transcrever.py --janela
  exit /b 0
)

echo.
echo [X] O Transcritor ainda nao foi instalado nesta pasta.
echo     Rode INSTALAR_casa.bat (se voce tem Python e e administrador)
echo     ou INSTALAR_sem_admin.bat (nos outros computadores).
echo.
pause
