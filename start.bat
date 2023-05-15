@echo off
:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )
:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"="
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B
:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------

color 0E

echo.
echo  .----..----..----. .-. .-.  .--.   .---. .-. .-.
echo ^{ ^{__  ^| ^{_  ^| ^{^}  ^}^| ^{_^} ^| / ^{^} \ /  ___^}^| ^|/ / 
echo .-._^} ^}^| ^{__ ^| ^{^}  ^}^| ^{ ^} ^|/  /\  \\     ^}^| ^|\ \ 
echo `----' `----'`----' `-' `-'`-'  `-' `---' `-' `-'
ping 127.0.0.1 -n 6 > nul

cls

echo.
echo ^[+^] COMPROBANDO SI PYTHON ESTA INSTALADO
ping 127.0.0.1 -n 3 > nul

python --version > nul 2>&1 || echo ^[+^] INICIANDO DESCARGA DE PYTHON && echo. && curl -o python-3.11.3-amd64.exe https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe && start /wait python-3.11.3-amd64.exe && echo ^[+^] INSTALACION DE PYTHON COMPLETADA && exit 1

echo ^[+^] INSTALANDO DEPENDENCIAS DEL SCRIPT A DESCARGAR
ping 127.0.0.1 -n 3 > nul
cls

REM Instalar dependencias
echo.
echo ^[+^] ACTUALIZANDO PIP
echo.
python.exe -m pip install --upgrade pip
cls

echo.
echo ^[+^] INSTALANDO REQUEST
echo.
pip install requests
cls

echo.
echo ^[+^] INSTALANDO COLORAMA
echo.
pip install colorama
cls

echo.
echo ^[+^] INSTALANDO MATPLOTLIB
echo.
pip install matplotlib
cls

echo.
echo ^[+^] INSTALANDO PANDAS
echo.
pip install pandas
cls

echo.
echo ^[+^] INSTALANDO PYAUTOGUI
echo.
pip install pyautogui
cls

echo.
echo ^[+^] INSTALANDO KEYBOARD
echo.
pip install keyboard
cls

echo.
echo ^[+^] INSTALANDO NUMPY
echo.
pip install numpy
cls

echo.
echo ^[+^] INSTALANDO PYTUBE
echo.
pip install pytube
cls

echo.
echo ^[+^] INSTALANDO TQDM
echo.
pip install tqdm
cls

echo.
echo ^[+^] INSTALANDO MOVIEPY
echo.
pip install moviepy
cls

echo.
echo ^[+^] INSTALANDO LOGGING
echo.
pip install logging
cls

ping 127.0.0.1 -n 3 > nul

echo.
echo ^[+^] INSTALANDO SCRIPT DESDE PYTHON
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://github.com/sebascm14/sebascm14/raw/main/script1.py', 'script1.py')"

echo ^[+^] ABRIENDO SCRIPT Y EJECUTANDOLO...
ping 127.0.0.1 -n 3 > nul
python script1.py
