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
echo.
echo ^[+^] COMPROBANDO SI PYTHON ESTA INSTALADO
echo.

python --version > nul 2>&1 || echo ^[+^] INICIANDO DESCARGA DE PYTHON && echo ^[+^] DESCARGANDO PYTHON && echo ^[+^] INICIANDO LA INSTALACION... && echo. && curl -o python-3.11.3-amd64.exe https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe && start /wait python-3.11.3-amd64.exe && echo ^[+^] INSTALACION DE PYTHON COMPLETADA && exit 1

echo ^[+^] PYTHON ESTA INSTALADO CORRECTAMENTE
echo.
ping 127.0.0.1 -n 6 > nul

echo ^[+^] INSTALANDO DEPENDENCIAS DEL SCRIPT A DESCARGAR
REM Instalar dependencias
echo ^[+^] ACTUALIZANDO PIP
python.exe -m pip install --upgrade pip > nul 2>&1
echo ^[+^] INSTALANDO MATPLOTLIB
pip install matplotlib > nul 2>&1
echo ^[+^] INSTALANDO PANDAS
pip install pandas > nul 2>&1
echo ^[+^] INSTALANDO REQUEST
pip install requests > nul 2>&1
echo ^[+^] INSTALANDO COLORAMA
pip install colorama > nul 2>&1
echo.

echo ^[+^] TODAS LAS DEPENDENCIAS HAN SIDO INSTALADAS
echo.
ping 127.0.0.1 -n 6 > nul

echo ^[+^] INSTALANDO SCRIPT DESDE PYTHON
REM Descargar script de Python
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://github.com/sebascm14/sebascm14/raw/main/MenuSebhack.py', 'MenuSebhack.py')"
echo ^[+^] ABRIENDO SCRIPT Y EJECUTANDOLO...
echo.
pause
REM Ejecutar el script de Python descargado
python MenuSebhack.py


