@echo off
chcp 65001 >nul
title Instalador do Transcritor - sem instalar nada no Windows
cd /d "%~dp0"
echo.
echo ==========================================================
echo  Instalando o Transcritor SEM precisar de administrador
echo  Tudo fica dentro desta pasta. Nada e instalado no Windows.
echo ==========================================================
echo.

set PY=%~dp0python-portatil\python.exe

if exist "%PY%" goto :tempython
echo [1/5] Baixando um Python portatil (cerca de 15 MB)...
powershell -NoProfile -Command "$ErrorActionPreference=Stop; Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.9/python-3.11.9-embed-amd64.zip -OutFile python.zip" || goto :erro

echo [2/5] Descompactando...
powershell -NoProfile -Command "$ErrorActionPreference=Stop; Expand-Archive -Path python.zip -DestinationPath python-portatil -Force" || goto :erro
del python.zip
powershell -NoProfile -Command "$ErrorActionPreference=Stop; $f=Get-ChildItem python-portatil\*._pth; (Get-Content $f.FullName) -replace ^#import site,import site | Set-Content $f.FullName" || goto :erro

:tempython
echo [3/5] Preparando o instalador de pacotes...
if not exist "python-portatil\Scripts\pip.exe" (
  powershell -NoProfile -Command "$ErrorActionPreference=Stop; Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py" || goto :erro
  "%PY%" get-pip.py --quiet || goto :erro
  del get-pip.py
)

echo [4/5] Baixando as pecas (yt-dlp e Whisper). Pode demorar alguns minutos...
"%PY%" -m pip install --quiet -r requirements.txt || goto :erro

echo [5/5] Ajustando para computador sem placa de video...
powershell -NoProfile -Command "(Get-Content config.json) -replace \"modelo\": \"medium\",\"modelo\": \"small\" | Set-Content config.json" 2>nul
echo     (usando o modelo rapido, porque esta maquina nao tem placa dedicada)

echo.
echo Pronto. Para usar, e so dar dois cliques em Transcritor.bat
echo.
pause
exit /b 0

:erro
echo.
echo [X] A instalacao falhou no passo acima.
echo     Copie a mensagem de erro inteira e mande para o Claude.
echo.
pause
exit /b 1
