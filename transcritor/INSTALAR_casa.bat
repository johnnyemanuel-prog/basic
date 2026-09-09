@echo off
chcp 65001 >nul
title Instalador do Transcritor - maquina com Python
cd /d "%~dp0"
echo.
echo ===============================================
echo  Instalando o Transcritor (maquina com Python)
echo ===============================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
  echo [X] Python nao encontrado neste computador.
  echo     Use o outro arquivo: INSTALAR_sem_admin.bat
  echo.
  pause
  exit /b 1
)

echo [1/4] Criando o ambiente isolado...
python -m venv ambiente || goto :erro

echo [2/4] Atualizando o instalador de pacotes...
ambiente\Scripts\python.exe -m pip install --upgrade pip --quiet || goto :erro

echo [3/4] Baixando as pecas (yt-dlp e Whisper). Pode demorar alguns minutos...
ambiente\Scripts\python.exe -m pip install --quiet -r requirements.txt || goto :erro

echo [4/4] Instalando o suporte a placa NVIDIA (deixa a transcricao bem mais rapida)...
ambiente\Scripts\python.exe -m pip install --quiet nvidia-cublas-cu12 nvidia-cudnn-cu12
if errorlevel 1 echo     [aviso] nao deu para instalar o suporte a NVIDIA. Vai funcionar mesmo assim, so mais devagar.

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
