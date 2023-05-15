import ctypes
import sys
import os
import time
import subprocess
import winreg
import requests
import zipfile
import pyautogui as pt
import numpy as np
import keyboard
import time
import random
from pytube import Playlist
from tqdm import tqdm
import moviepy.editor as mp
import logging
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
    print(Fore.GREEN + '97. Descargas Multimedia' + Style.RESET_ALL)
    print(Fore.GREEN + '98. Sorteos Instagram Automatizado' + Style.RESET_ALL)
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

    elif opcion == '97':

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW + '╔══════════════════════╗' + Style.RESET_ALL)
            print(Fore.YELLOW + '║ DESCARGAS MULTIMEDIA ║' + Style.RESET_ALL)
            print(Fore.YELLOW + '╚══════════════════════╝' + Style.RESET_ALL)
            print()
            print(Fore.GREEN + '1. DESARROLLANDO' + Style.RESET_ALL)
            print(Fore.GREEN + '2. DESARROLLANDO' + Style.RESET_ALL)
            print(Fore.GREEN + '3. DESCARGAR PLAYLSIT MP4 YOUTUBE' + Style.RESET_ALL)
            print(Fore.GREEN + '4. DESCARGAR PLAYLIST MP3 YOUTUBE' + Style.RESET_ALL)
            print(Fore.RED + '99. Volver' + Style.RESET_ALL)
            print()

            opcionEntretenimiento = input('Seleccione una opcion: ')

            if opcionEntretenimiento == '1':
                print()
                print(Fore.YELLOW + 'DESARROLLANDO...' + Style.RESET_ALL)
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')

            elif opcionEntretenimiento == '2':
                print()
                print(Fore.YELLOW + 'DESARROLLANDO...' + Style.RESET_ALL)
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
            
            elif opcionEntretenimiento == '3':
                
                # Disable moviepy logs
                logger = logging.getLogger('moviepy')
                logger.setLevel(logging.ERROR)
                logging.disable(logging.WARNING)
                logging.disable(logging.CRITICAL)
                logging.disable(logging.INFO)

                def sanitize_filename(filename):
                    """
                    Elimina caracteres no permitidos en nombres de archivo de Windows.
                    """
                    forbidden_chars = r'<>:"/\|?*'
                    for char in forbidden_chars:
                        filename = filename.replace(char, '')
                    return filename

                def download_playlist_videos():
                    os.system('cls' if os.name == 'nt' else 'clear')

                    print(Fore.YELLOW + '╔════════════════════════════════╗' + Style.RESET_ALL)
                    print(Fore.YELLOW + '║ DESCARGAR PLAYLIST MP4 YOUTUBE ║' + Style.RESET_ALL)
                    print(Fore.YELLOW + '╚════════════════════════════════╝' + Style.RESET_ALL)
                    print()

                    playlist_url = input("Ingrese la URL de la Playlist: ")

                    pl = Playlist(playlist_url)
                    
                    # Obtener el título de la lista de reproducción
                    playlist_title = sanitize_filename(pl.title)
                    
                    # Crear la carpeta principal con el nombre "Playlist" si no existe
                    main_folder = "Playlist"
                    if not os.path.exists(main_folder):
                        os.makedirs(main_folder)
                    
                    # Crear la carpeta con el título de la lista de reproducción dentro de la carpeta principal
                    folder_name = sanitize_filename(playlist_title.replace('/', '_'))
                    folder_path = f"{main_folder}/{folder_name}"
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    
                    total_videos = len(pl.video_urls)
                    
                    for index, video in enumerate(pl.videos, start=1):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(Fore.YELLOW + '╔════════════════════════════════╗' + Style.RESET_ALL)
                        print(Fore.YELLOW + '║ DESCARGAR PLAYLIST MP4 YOUTUBE ║' + Style.RESET_ALL)
                        print(Fore.YELLOW + '╚════════════════════════════════╝' + Style.RESET_ALL)
                        print()
                        print(Fore.YELLOW + f'[ PLAYLIST {playlist_title} ]' + Style.RESET_ALL)
                        print()

                        print(Fore.YELLOW + '[/]' + Style.RESET_ALL + f" DESCARGANDO {index} DE {total_videos}: {video.title}")
                        stream = video.streams.get_highest_resolution()
                        file_size = int(requests.head(stream.url).headers.get("Content-Length"))
                        
                        # Descargar el video con una barra de progreso
                        response = requests.get(stream.url, stream=True)
                        video_file_path = f"{folder_path}/{sanitize_filename(video.title)}.mp4"
                        mp3_file_path = f"{folder_path}/{sanitize_filename(video.title)}.mp3"
                        
                        with open(video_file_path, "wb") as f:
                            with tqdm(total=file_size, unit='bytes', unit_scale=True) as pbar:
                                for chunk in response.iter_content(chunk_size=1024):
                                    if chunk:
                                        f.write(chunk)
                                        pbar.update(len(chunk))

                        
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(Fore.YELLOW + '╔═══════════════════════════════╗' + Style.RESET_ALL)
                    print(Fore.YELLOW + '║ DESCARGAR PLAYLIST DE YOUTUBE ║' + Style.RESET_ALL)
                    print(Fore.YELLOW + '╚═══════════════════════════════╝' + Style.RESET_ALL)
                    print()
                    print(Fore.GREEN + f'[ PLAYLIST {playlist_title} DESCARGADA CORRECTAMENTE ]' + Style.RESET_ALL)
                    print()

                    for index, video in enumerate(pl.videos, start=1):
                        print(Fore.GREEN + '[+]' + Style.RESET_ALL + f" {video.title}")
                    
                    print()
                    print(Fore.GREEN + "[!]" + Style.RESET_ALL + " PRESIONA ENTER PARA VOLVER AL MENU")
                    input()

                try:
                    download_playlist_videos()
                except Exception as e:
                    print(f"Ocurrió un error durante la descarga: {str(e)}")

            
            elif opcionEntretenimiento == '4':

                # Disable moviepy logs
                logger = logging.getLogger('moviepy')
                logger.setLevel(logging.ERROR)
                logging.disable(logging.WARNING)
                logging.disable(logging.CRITICAL)
                logging.disable(logging.INFO)

                def sanitize_filename(filename):
                    """
                    Elimina caracteres no permitidos en nombres de archivo de Windows.
                    """
                    forbidden_chars = r'<>:"/\|?*'
                    for char in forbidden_chars:
                        filename = filename.replace(char, '')
                    return filename

                def download_playlist_videos():
                    os.system('cls' if os.name == 'nt' else 'clear')

                    print(Fore.YELLOW + '╔════════════════════════════════╗' + Style.RESET_ALL)
                    print(Fore.YELLOW + '║ DESCARGAR PLAYLIST MP3 YOUTUBE ║' + Style.RESET_ALL)
                    print(Fore.YELLOW + '╚════════════════════════════════╝' + Style.RESET_ALL)
                    print()

                    playlist_url = input("Ingrese la URL de la Playlist: ")

                    pl = Playlist(playlist_url)
                    
                    # Obtener el título de la lista de reproducción
                    playlist_title = sanitize_filename(pl.title)
                    
                    # Crear la carpeta principal con el nombre "Playlist" si no existe
                    main_folder = "Playlist"
                    if not os.path.exists(main_folder):
                        os.makedirs(main_folder)
                    
                    # Crear la carpeta con el título de la lista de reproducción dentro de la carpeta principal
                    folder_name = sanitize_filename(playlist_title.replace('/', '_'))
                    folder_path = f"{main_folder}/{folder_name}"
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    
                    total_videos = len(pl.video_urls)
                    
                    for index, video in enumerate(pl.videos, start=1):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(Fore.YELLOW + '╔════════════════════════════════╗' + Style.RESET_ALL)
                        print(Fore.YELLOW + '║ DESCARGAR PLAYLIST MP3 YOUTUBE ║' + Style.RESET_ALL)
                        print(Fore.YELLOW + '╚════════════════════════════════╝' + Style.RESET_ALL)
                        print()
                        print(Fore.YELLOW + f'[ PLAYLIST {playlist_title} ]' + Style.RESET_ALL)
                        print()

                        print(Fore.YELLOW + '[/]' + Style.RESET_ALL + f" DESCARGANDO {index} DE {total_videos}: {video.title}")
                        stream = video.streams.get_highest_resolution()
                        file_size = int(requests.head(stream.url).headers.get("Content-Length"))
                        
                        # Descargar el video con una barra de progreso
                        response = requests.get(stream.url, stream=True)
                        video_file_path = f"{folder_path}/{sanitize_filename(video.title)}.mp4"
                        mp3_file_path = f"{folder_path}/{sanitize_filename(video.title)}.mp3"
                        
                        with open(video_file_path, "wb") as f:
                            with tqdm(total=file_size, unit='bytes', unit_scale=True) as pbar:
                                for chunk in response.iter_content(chunk_size=1024):
                                    if chunk:
                                        f.write(chunk)
                                        pbar.update(len(chunk))
                        
                        # Convertir el video a MP3
                        try:
                            orig_stdout = sys.stdout
                            sys.stdout = open(os.devnull, 'w')  # Suprimir la salida
                            video_clip = mp.VideoFileClip(video_file_path)
                            audio_clip = video_clip.audio
                            audio_clip.write_audiofile(mp3_file_path, verbose=False)
                        finally:
                            sys.stdout.close()
                            sys.stdout = orig_stdout

                        # Cerrar los clips de video y audio
                        video_clip.close()
                        audio_clip.close()

                        # Eliminar el archivo MP4
                        os.remove(video_file_path)
                        
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(Fore.YELLOW + '╔═══════════════════════════════╗' + Style.RESET_ALL)
                    print(Fore.YELLOW + '║ DESCARGAR PLAYLIST DE YOUTUBE ║' + Style.RESET_ALL)
                    print(Fore.YELLOW + '╚═══════════════════════════════╝' + Style.RESET_ALL)
                    print()
                    print(Fore.GREEN + f'[ PLAYLIST {playlist_title} DESCARGADA CORRECTAMENTE ]' + Style.RESET_ALL)
                    print()

                    for index, video in enumerate(pl.videos, start=1):
                        print(Fore.GREEN + '[+]' + Style.RESET_ALL + f" {video.title}")
                    
                    print()
                    print(Fore.GREEN + "[!]" + Style.RESET_ALL + " PRESIONA ENTER PARA VOLVER AL MENU")
                    input()

                try:
                    download_playlist_videos()
                except Exception as e:
                    print(f"Ocurrió un error durante la descarga: {str(e)}")

            elif opcionEntretenimiento == '99':
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            else:
                print('Opción inválida')

    elif opcion == '98':
        
        os.system('cls' if os.name == 'nt' else 'clear')

        print(Fore.YELLOW + '╔══════════════════════════════════════╗' + Style.RESET_ALL)
        print(Fore.YELLOW + '║ PARTICIPANDO EN SORTEOS DE INSTAGRAM ║' + Style.RESET_ALL)
        print(Fore.YELLOW + '╚══════════════════════════════════════╝' + Style.RESET_ALL)
        time.sleep(2)
        print()

        print(Fore.YELLOW + '[/]' + Style.RESET_ALL + ' CONFIRMANDO SEGUIDOS DE LA CUENTA @_SEBASCM_')
        time.sleep(3)
        print()

        seguidos = np.array(["carmenchu_ligero", 
                    "robetanzos8", 
                    "gury_00", 
                    "vanesa.sanchez99", 
                    "joantica_", 
                    "isaariico",
                    "vitopicon",
                    "daconlo_photo",
                    "estherauta",
                    "manuelmartin94",
                    "anaturalwoman7",
                    "adribl_24",
                    "lauraavz_",
                    "cafecopas_sevilla9",
                    "iraidepe",
                    "victormelida",
                    "gomezcabrerana",
                    "martiitacabrera",
                    "tereesaprz_",
                    "javimunozdeejay",
                    "albeertt99",
                    "juanan__1999",
                    "celiamz00",
                    "oscarromerobenitez",
                    "fernandogarciatrigo",
                    "laleonstudio",
                    "druni_perfumerias",
                    "raydpics",
                    "noemimgr",
                    "swevenus",
                    "_anagonz",
                    "estiloextra",
                    "ulresch",
                    "_dariorhl",
                    "lalauraa5_",
                    "vaniabernaal",
                    "yeneira_1822",
                    "elfimous",
                    "luciacarrera0",
                    "celiablandonr",
                    "alfonsomrl_",
                    "aljequesitorico",
                    "hugotovar05",
                    "davidmartinlopez8",
                    "_celiiaprivv.01_",
                    "ivanvr03_",
                    "roxanamc.8",
                    "marianoogd",
                    "lidiacontrerass_",
                    "andigo99_",
                    "pmnzz_",
                    "aangelacontrerass",
                    "4_paulii",
                    "noxpadel",
                    "hensss",
                    "alejandro_06f",
                    "_andreaa.26_",
                    "lyaaruiz",
                    "ainhoapdll03",
                    "sandramugar",
                    "carlospiconn_",
                    "noemiiroosadoovaa0_",
                    "una_casita_en_la_montana",
                    "ariadna03_mulaaaa15",
                    "ines_cano99",
                    "its_japeco",
                    "_carmen.b.m_",
                    "pablogonzleez",
                    "crislv_02",
                    "franbulloon",
                    "aliciavb00",
                    "aangelacontreras_",
                    "anapavonnn02",
                    "fuliandreo",
                    "miguerb01",
                    "mariabrodriguezzz_",
                    "auroraparralo",
                    "claudia.martinez",
                    "taniadeniz_",
                    "dark_artsy_soul",
                    "jaimebenitez2002",
                    "nicesetupdude",
                    "naayraoj",
                    "aitanailss_",
                    "elenaajimenezz__",
                    "victorcruz_99",
                    "maariiaacg02",
                    "diego_lagares",
                    "mercedes_sr_",
                    "fran_ligero06",
                    "mariacarrasco018",
                    "lolarincon_",
                    "mariacg215",
                    "_marta_019",
                    "_luciiia22",
                    "_pabloramoss",
                    "carrlagomezz",
                    "cafepubnuevaera",
                    "nachommt_",
                    "_rcbeatriz08",
                    "jimenezperez98",
                    "manuuu_1985",
                    "jacus070",
                    "pulgar20",
                    "blord12s13",
                    "patrilagares",
                    "luciamreno",
                    "jesusgm12_",
                    "alvaromc_004",
                    "martsssanchez",
                    "chloeegomezzz",
                    "lauritaagonzalez_",
                    "rociogarridojm",
                    "beatrizedreira",
                    "_rubiio_07",
                    "luciiaa_boza",
                    "pccomponentes",
                    "waynabox",
                    "tuhjose7",
                    "rodri_gomez12",
                    "metodofitnesscoach",
                    "fuenteclaracabr",
                    "mireyamerchante_",
                    "_juliiarmro0_",
                    "miriamrddrgz",
                    "__alee__03",
                    "carmenleon97",
                    "javiermcc_",
                    "blupuertosherry",
                    "_angelapeerezz",
                    "luciaaspinola",
                    "dailyminecraftvibe",
                    "verogarcia00",
                    "mariosp_27",
                    "perciopelo",
                    "_juliomrtn_",
                    "paaulacorderoo",
                    "esthermr._",
                    "juliadominnguez_",
                    "_lamonterito_",
                    "theshoppingexpert",
                    "mariaperea00",
                    "adil._96",
                    "vanesa.sanchez99",
                    "lidiaa_2707",
                    "90alexx90",
                    "elenavillaran99",
                    "_juanjesg",
                    "amroestudiantes",
                    "carlajimenezz_",
                    "mariaenriquez",
                    "nuriagallardo01",
                    "_mriagonzalez0",
                    "patriiciapg_",
                    "corbacholife",
                    "_paulafdz_",
                    "_margamarin_",
                    "_teresaalarios",
                    "guiille_.7",
                    "loreglez_0",
                    "juanmafdz_19",
                    "miri_mph",
                    "carmen_gc8",
                    "nayramartiinez__",
                    "christian_hopf",
                    "antoniopicon5",
                    "elenapadilla99",
                    "sdjmalik",
                    "chuyandreaa",
                    "ainhoapadilla03",
                    "giines.zl",
                    "aithorrrr",
                    "s4vitarx",
                    "josenogaless",
                    "aandreeagarcia_",
                    "helloomonday",
                    "padelnuestro",
                    "nomadingcamp",
                    "blancagonzalez7",
                    "lorena_rg29",
                    "patriestrella17",
                    "somosrevel",
                    "carmenchu_ligero",
                    "lacampillos",
                    "f_e_n_d",
                    "pauu_vldrs",
                    "dragos.004",
                    "ainoamora_",
                    "eduardomoratin",
                    "paulapc01",
                    "sophieromein",
                    "andrea_hr01",
                    "mariia_jromero03",
                    "elisabeth17rb",
                    "erm_barber",
                    "minerva_sv_",
                    "mireiagonzalez7_",
                    "aliciaajmnezz_",
                    "caarmensanchez_29",
                    "luciabarroso02",
                    "laauravelo",
                    "_mariaperea",
                    "guillermo_md12",
                    "lauhfp",
                    "techno_gadze",
                    "caritoalaparato",
                    "alvaro_gon02",
                    "livepuntagraduaciones",
                    "luciaarosalees",
                    "armadaesp",
                    "iamcristinini",
                    "el_neeem",
                    "gal.law",
                    "inmacampanoo",
                    "tuli_acosta",
                    "martiss.s",
                    "angelaramosl_",
                    "_nessy97_",
                    "mariiadiazz05_",
                    "rebecadiiazz_",
                    "vanesaahp",
                    "nora_black",
                    "saaiii_05",
                    "azucenadmnguez_",
                    "lauragarciaaa01",
                    "celiasosa12",
                    "laurittadeluxe",
                    "gabrielnb18_",
                    "_adriiaan_27",
                    "cintii_rodriiguez",
                    "benito_rociin_",
                    "andrreaapalazon_",
                    "danieljaramillo1",
                    "aleexiaib",
                    "iireneperez_",
                    "_.carlajimeeneezz._",
                    "camilaagracia",
                    "andreacobos_",
                    "danielacorss",
                    "anabd01",
                    "mariatorressg",
                    "mariamazadl",
                    "almudenaruiiz__",
                    "ireland_paula",
                    "nattaliiaa00",
                    "paulaa.lorena",
                    "geeemamf",
                    "_alexprgl_",
                    "erpildora_18",
                    "dragonf_j",
                    "celia.cres",
                    "daviiear",
                    "jesper.clo",
                    "martacano16",
                    "nolanomura",
                    "nicolrojas201",
                    "_celialpz_",
                    "pervincaje",
                    "ruroc_spain",
                    "edurm_00",
                    "ermbarber_",
                    "alvarogr___",
                    "dios",
                    "kiaruu_u",
                    "lauragarrotee",
                    "mariialopeez01",
                    "sandraagbp",
                    "aly_aleeee",
                    "claralopezz98_",
                    "johanna_barroso",
                    "_lauuragf_",
                    "elisawaves",
                    "carmenrd24",
                    "aanabeleneiro",
                    "squadkoi",
                    "micro__terra",
                    "tara.hdzz",
                    "saracnmrtl",
                    "anddrearojas",
                    "yleniaortegapadron",
                    "ariiadnadelpiino",
                    "anaa.arrabal",
                    "albaastn",
                    "irinijannouliss",
                    "zzmariaruizzz",
                    "soofiquintanaa",
                    "sntnnivi_",
                    "soniajmnz_g",
                    "carmeen_mar",
                    "pipiopaula",
                    "maariiaabaez",
                    "aliciaag25",
                    "andreacaldem",
                    "andreapgmitimi",
                    "sergioberesaluze",
                    "anarng8",
                    "estrellaturmo",
                    "canitaa_fernandez",
                    "adrianalgrs",
                    "alessl10",
                    "daviniapm2",
                    "belenmongee",
                    "carmenrc_98",
                    "nnereaescudero",
                    "_lauragarciab",
                    "pam.lopz",
                    "bbrunno_sp",
                    "cristinadazaa",
                    "blancadelvalle_",
                    "maddiemorenoo",
                    "soffiazc",
                    "carolytoni04",
                    "almuudeenaa18__",
                    "soyinap",
                    "claralpezx2",
                    "saraarobles_06",
                    "mariiamv_15",
                    "doribautista_",
                    "mariapalomo0",
                    "noeliarocr_01",
                    "mariakatycat12",
                    "annaina._",
                    "2defarfolla",
                    "luugrdill",
                    "estelahermo",
                    "jonilozano_15",
                    "princesadelpoli",
                    "roruizzz_",
                    "_ljv22",
                    "__pablocamsal",
                    "angeliicadzz_",
                    "guardiacivil062",
                    "espepr14",
                    "_elparrafo",
                    "_aliivalenciano",
                    "mvmg_04",
                    "fernandov.4",
                    "antonio.4",
                    "albsalmar_05",
                    "paolablazquezz",
                    "_mpgarcia04",
                    "beaatrizleal",
                    "teacheradriana1",
                    "luciapastranaf",
                    "thecarolos",
                    "xiaomiespana",
                    "esenziaclub",
                    "veronicaburgos_00",
                    "miriamzuritagar",
                    "ainhoaparrenho",
                    "rebelsfest",
                    "antonio.carlos_31",
                    "claramaartineez_",
                    "ikermac_",
                    "tanechkaozolina",
                    "themotographer",
                    "recambiosalcorte",
                    "bmwmotorrad",
                    "ktm_official",
                    "hondamotoses",
                    "aprilia",
                    "ducatiesp",
                    "yamahamotor_es",
                    "kawasaki_espana",
                    "free.rap.argento",
                    "motorcyclediary0",
                    "erikagomeezz_",
                    "hookah._medaigual",
                    "robert_marius_gh",
                    "sorianoojeda0",
                    "oharasoriano",
                    "so____cold",
                    "rachid_r06",
                    "pablocl251",
                    "mariagllgo_",
                    "martaajlpz_",
                    "jordimb_18",
                    "neereeaaml",
                    "gloriahuelva24",
                    "teresasalas_22",
                    "belengme",
                    "damian_varelita",
                    "laurafergonza",
                    "elenaraposso",
                    "tinistoessel",
                    "josebarreradj",
                    "nataaparamontaar",
                    "dani3l_ramoos",
                    "denismicu_",
                    "lauralunam_",
                    "carmenpicana",
                    "anadoorado",
                    "daavidclavijoo",
                    "blancaarg5",
                    "teresaapascual",
                    "ireneslvaa",
                    "belencastill0_",
                    "elenacamachoo_",
                    "pablo_sd01",
                    "santi_rff",
                    "marinadominguez_12",
                    "inesguillen_",
                    "belencaba_02",
                    "race_svq",
                    "javialanis8",
                    "patricia_m10",
                    "espee_25",
                    "rocioshdez_",
                    "javieresquilichem_",
                    "mariasanchez022",
                    "violetamunz",
                    "roci_bizzle_",
                    "teresamunozdlrosa",
                    "angelaav02",
                    "albiitadiiaz_",
                    "juanisaac9307",
                    "carlosrosu99",
                    "sabiinaa_g",
                    "maria_maaldonado",
                    "_beaperezz_",
                    "beatrizfdezz_",
                    "ag.romeroo_",
                    "alebenitz_",
                    "martaagarrciaa",
                    "ramoncortes25",
                    "davidsp_19",
                    "vickyjm",
                    "_luciabc_",
                    "jpl__7",
                    "manuromeroo02",
                    "rociobesteiro",
                    "elenaajjmeneez_",
                    "aitanadauphin",
                    "luciluumm",
                    "13estelajapon",
                    "laura__castellano",
                    "aerensatierf",
                    "nazaretct13",
                    "nataliabtsta_",
                    "_marinarg8",
                    "lauramsosa_",
                    "_anxxrs_",
                    "paula.tejadaa",
                    "cyntthiaa_14",
                    "marta_bunny_",
                    "_jajajajajajaj2",
                    "cristinaherca01",
                    "_maaripaz",
                    "aaitaanaa.perez",
                    "saaraasaanchez_",
                    "mayloboxx",
                    "_lauurasalas_",
                    "monicaportafax",
                    "21cbab__",
                    "ksikierokesitengo",
                    "rociioo_b02",
                    "andreaamartinm_",
                    "lucianevado3",
                    "lo_azucar_ve",
                    "saraahaldon",
                    "beatrizalarconn",
                    "juliacastanedaa",
                    "sergio_veil",
                    "heleena06",
                    "slurmpled",
                    "elenaramos_",
                    "belssai_",
                    "mariiasagrarioo",
                    "gloriamarquezz_",
                    "juangarciaa2",
                    "leopm3_",
                    "autoesculaloshermanos",
                    "mariaamc__",
                    "alejandraps006",
                    "luciavillaran_",
                    "bertalgrs_",
                    "yanirarm_",
                    "fatiii_gl7",
                    "ainhoaacaceeres",
                    "bengalaspain",
                    "cristii_fit",
                    "padel0limites",
                    "padel.spain",
                    "navarro_paquito",
                    "verseapp",
                    "mister_jagger",
                    "carlaadp_",
                    "papaspanas_123",
                    "ezequiel__cee",
                    "a.s.c_0",
                    "marinapalma_",
                    "paularamooss_",
                    "fitnessbymery",
                    "marianitaarceleon",
                    "mtlaura1",
                    "fatimavillaran_",
                    "ylenia_ls_05",
                    "themariquilla",
                    "candelapetrash",])

        limit = len(seguidos)
        i = 0

        print(Fore.YELLOW + '[/]' + Style.RESET_ALL + ' COLOCA EL CURSOR DONDE QUIERAS ESCRIBIR LOS SEGUIDORES')
        time.sleep(1)
        print()

        print(Fore.YELLOW + '[/]' + Style.RESET_ALL + ' PROGRAMA PAUSADO ESPERANDO CONFIRMACION DEL USUARIO, PULSA PARA CONTINUAR')
        input()
        print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' EMPEZANDO LA INSERCCION DE USUARIOS EN DONDE ESTA EL CURSOR (5seg)')
        print('----------------------------------------------------------------------')
        print()
        time.sleep(5)
        
        while i < limit:
            print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' USUARIO:', seguidos[i])
            keyboard.press_and_release("altgr+2")
            pt.typewrite(str(seguidos[i]))
            pt.press("enter")
            tiempo_espera = random.uniform(10, 120)  # 20 segundos = 0.33 minutos, 300 segundos = 5 minutos
            time.sleep(tiempo_espera)
            i += 1

        print()
        print('----------------------------------------------------------------------')
        print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' LA INSERCCION DE USUARIOS HA FINALIZADO, PULSE PARA VOLVER AL MENU')
        input()
        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcion == '99':
        print('Saliendo...')
        sys.exit()
    
    else:
        print('Opción inválida')
        sys.exit()
