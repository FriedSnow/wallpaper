import ctypes
import os
import time
from PIL import Image, ImageChops

# Получаем путь к файлу обоев
appdata_folder = os.getenv('APPDATA')

current_path = os.path.join(appdata_folder, 'Microsoft', 'Windows', 'Themes', 'TranscodedWallpaper')
target_path = r'C:\Users\Alexander\Desktop\sutridtsat.jpg'
new_path = r'C:\Users\Alexander\Desktop\mirage.jpg'  # Путь к новым обоям

# Открываем файл обоев с помощью Pillow
current_image = Image.open(current_path)
target_image = Image.open(target_path)
new_image = Image.open(new_path)

def set_wallpaper(image_path):
    # Константы для функции SystemParametersInfo
    SPI_SETDESKWALLPAPER = 0x0014
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02

    # Вызов функции SystemParametersInfo для изменения обоев рабочего стола
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)

def check():
    if current_image.mode == target_image.mode and current_image.size == target_image.size:
        difference = ImageChops.difference(current_image, target_image).getbbox()
        set_wallpaper(new_path)
        print('ХХЫХЫХЫХЫХЫХЫХАХАХААХ')

check()