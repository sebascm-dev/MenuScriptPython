import ctypes
import sys
import os
import time
import subprocess
import winreg
import requests
import zipfile
from colorama import init, Fore, Style

# Función para elevar los privilegios del script a nivel de administrador
def elevate_privileges():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        # Si el usuario no tiene privilegios de administrador, intenta elevar los privilegios
        # Ejecuta el script de nuevo con el parámetro 'runas' para solicitar los permisos de administrador
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

# Llamar a la función para elevar los privilegios
elevate_privileges()

# A partir de aquí, el script tiene privilegios de administrador
# Puedes poner aquí el código que necesita privilegios de administrador

def win32_check_os():
    # Leer la clave de registro que contiene información sobre la edición de Windows
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion") as key:
            edition_id = winreg.QueryValueEx(key, "EditionID")[0]
    except:
        edition_id = ""

    return edition_id

# Obtener el nombre de la edición de Windows
edicion_windows = win32_check_os()

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print(Fore.YELLOW + '╔═════════════════════════════════╗' + Style.RESET_ALL)
    print(Fore.YELLOW + '║ MENU DE CONFIGURACION PRINCIPAL ║' + Style.RESET_ALL)
    print(Fore.YELLOW + '╚═════════════════════════════════╝' + Style.RESET_ALL)
    print()
    print(Fore.GREEN + '1. Activaciones Windows' + Style.RESET_ALL)
    print(Fore.GREEN + '2. Descargar Office-2021' + Style.RESET_ALL)
    print(Fore.RED + '99. Salir' + Style.RESET_ALL)
    print()

    opcion = input('Seleccione una opcion: ')

    if opcion == '1':

        os.system('cls' if os.name == 'nt' else 'clear')

        while True:
            print(Fore.YELLOW + '╔═════════════════════════╗' + Style.RESET_ALL)
            print(Fore.YELLOW + '║ ACTIVACIONES DE WINDOWS ║' + Style.RESET_ALL + ' EDICION: Windows', edicion_windows)
            print(Fore.YELLOW + '╚═════════════════════════╝' + Style.RESET_ALL)
            print()
            print(Fore.GREEN + '1. Activar Windows PRO' + Style.RESET_ALL)
            print(Fore.GREEN + '2. Activar Windows HOME' + Style.RESET_ALL)
            print(Fore.RED + '99. Volver' + Style.RESET_ALL)
            print()

            opcionActivacion = input('Seleccione una opcion: ')

            if opcionActivacion == '1':

                os.system('cls' if os.name == 'nt' else 'clear')

                print(Fore.YELLOW + '╔═══════════════════════════╗' + Style.RESET_ALL)
                print(Fore.YELLOW + '║ ACTIVACION DE WINDOWS PRO ║' + Style.RESET_ALL)
                print(Fore.YELLOW + '╚═══════════════════════════╝' + Style.RESET_ALL)
                print()
                time.sleep(2)

                print(Fore.YELLOW + '[/]' + Style.RESET_ALL + ' EJECUTANDO EL COMANDO: slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')
                subprocess.run(['slmgr', '/ipk', 'W269N-WFGWX-YVC9B-4J6C9-T83GX'], shell=True)
                print(Fore.YELLOW + '[/]' + Style.RESET_ALL + ' EJECUTANDO EL COMANDO: slmgr /skms kms.digiboy.ir')
                subprocess.run(['slmgr', '/skms', 'kms.digiboy.ir'], shell=True)
                print(Fore.YELLOW + '[/]' + Style.RESET_ALL + ' EJECUTANDO EL COMANDO: slmgr /ato')
                subprocess.run(['slmgr', '/ato'], shell=True)
                print()

                print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' LA ACTIVACION HA FINALIZADO CORRECTAMENTE')
                print()
                time.sleep(2)
                
                os.system('cls' if os.name == 'nt' else 'clear')


            elif opcionActivacion == '2':

                os.system('cls' if os.name == 'nt' else 'clear')

                print(Fore.YELLOW + '╔════════════════════════════╗' + Style.RESET_ALL)
                print(Fore.YELLOW + '║ ACTIVACION DE WINDOWS HOME ║' + Style.RESET_ALL)
                print(Fore.YELLOW + '╚════════════════════════════╝' + Style.RESET_ALL)
                print()
                time.sleep(2)

                print(Fore.YELLOW + '[/]' + Style.RESET_ALL + ' EJECUTANDO EL COMANDO: slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99')
                subprocess.run(['slmgr', '/ipk', 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99'], shell=True)
                print(Fore.YELLOW + '[/]' + Style.RESET_ALL + ' EJECUTANDO EL COMANDO: slmgr /skms kms.digiboy.ir')
                subprocess.run(['slmgr', '/skms', 'kms.digiboy.ir'], shell=True)
                print(Fore.YELLOW + '[/]' + Style.RESET_ALL + ' EJECUTANDO EL COMANDO: slmgr /ato')
                subprocess.run(['slmgr', '/ato'], shell=True)
                print()

                print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' LA ACTIVACION HA FINALIZADO CORRECTAMENTE')
                print()
                time.sleep(2)
                
                os.system('cls' if os.name == 'nt' else 'clear')

            elif opcionActivacion == '99':
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            else:
                print('Opción inválida')


    elif opcion == '2':
        
        os.system('cls' if os.name == 'nt' else 'clear')

        print(Fore.YELLOW + '╔══════════════════════════════╗' + Style.RESET_ALL)
        print(Fore.YELLOW + '║ INSTALACION DE OFFICE - 2021 ║' + Style.RESET_ALL)
        print(Fore.YELLOW + '╚══════════════════════════════╝' + Style.RESET_ALL)
        print()

        # Desactivar la monitorización en tiempo real
        print(Fore.RED + '[-]' + Style.RESET_ALL + ' DESACTIVANDO LA PROTECCION EN TIEMPO REAL')
        comando = "powershell -command \"Set-MpPreference -DisableRealtimeMonitoring $true\""
        subprocess.run(comando, shell=True)
        # Desactivar la protección basada en la nube
        print(Fore.RED + '[-]' + Style.RESET_ALL + ' DESACTIVANDO LA PROTECCION BASADA EN LA NUBE')
        comando = "powershell -command \"Set-MpPreference -CloudBlockLevel 0\""
        subprocess.run(comando, shell=True)
        # Desactivar el envío de muestras automáticamente
        print(Fore.RED + '[-]' + Style.RESET_ALL + ' DESACTIVANDO EL ENVIO DE MUESTRAS AUTOMATICAMENTE')
        comando = "powershell -command \"Set-MpPreference -MAPSReporting 0\""
        subprocess.run(comando, shell=True)
        # Desactivar la protección contra alteraciones
        print(Fore.RED + '[-]' + Style.RESET_ALL + ' DESACTIVANDO LA PROTECCION CONTRA ALTERACIONES')
        comando = "powershell -command \"Set-MpPreference -DisableBehaviorMonitoring $true\""
        subprocess.run(comando, shell=True)
        print()


        # Descargar
        print(Fore.YELLOW + '[/]' + Style.RESET_ALL + ' DESCARGANDO OFFICE-2021.ZIP')
        url = 'https://github.com/sebascm14/sebascm14/raw/main/Office%202021.zip'
        archivo_destino = 'Office 2021.zip'

        response = requests.get(url)

        with open(archivo_destino, 'wb') as f:
            f.write(response.content)
        
        # Descomprimir
        print(Fore.YELLOW + '[/]' + Style.RESET_ALL + ' DESCOMPRIMIENDO ARCHIVO...')
        with zipfile.ZipFile(archivo_destino, 'r') as zip_ref:
            zip_ref.extractall('.')

        # Instalar
        print(Fore.YELLOW + '[/]' + Style.RESET_ALL + ' ARCHIVO DESCOMPRIMIDO...')
        time.sleep(2)

        # Ejecutar
        print(Fore.YELLOW + '[/]' + Style.RESET_ALL + ' EJECUTANDO OFFICE 2021')
        print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' INSTALANDO...')
        os.system('cmd /c "cd OFFICE 2021 && setup.exe /configure configuration.xml"')

        print()
        print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' EL SOFTWARE DE OFFICE HA SIDO INSTALADO CORRECTAMENTE')
        time.sleep(3)

        os.system('cls' if os.name == 'nt' else 'clear')


    elif opcion == '99':
        print('Saliendo...')
        sys.exit()
    
    else:
        print('Opción inválida')
        sys.exit()
