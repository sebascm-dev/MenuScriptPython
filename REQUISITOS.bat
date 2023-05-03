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

python --version > nul 2>&1 || (powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe', 'python-3.11.3-amd64.exe')" && start python-3.11.3-amd64.exe /quiet /norestart && shutdown /r /t 0)

REM Instalar dependencias
python.exe -m pip install --upgrade pip > nul 2>&1
pip show pandas > nul 2>&1 || pip install pandas
pip show matplotlib > nul 2>&1 || pip install matplotlib
pip show ctypes > nul 2>&1 || pip install ctypes
pip show requests > nul 2>&1 || pip install requests
pip show colorama > nul 2>&1 || pip install colorama

REM Descargar script de Python
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://github.com/sebascm14/sebascm14/raw/main/Menu1.py', 'Menu1.py')"

REM Ejecutar el script de Python descargado
python Menu1.py


