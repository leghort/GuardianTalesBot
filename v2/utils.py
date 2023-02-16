import subprocess
from os import remove
from easyocr import Reader
from PIL import Image


ADB_SERVER_PATH = r"D:\Program Files\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe"

def tap_screen(x, y):
    command = [ADB_SERVER_PATH, "shell", "input", "tap", str(x), str(y)]
    subprocess.run(command)

def swipe_screen(start_x, start_y, end_x, end_y, duration):
    command = [ADB_SERVER_PATH, "shell", "input", "swipe", str(start_x), str(start_y), str(end_x), str(end_y), str(duration)]
    subprocess.run(command)

def search_string_on_screenshot(left: float, upper: float, right: float, bottom: float, search_string: str, deviceAddress="localhost:7555") -> bool:
    # Capture d'écran
    img = ".screenshot.png"
    command = [ADB_SERVER_PATH, "-s", deviceAddress, "exec-out", "screencap", "-p"]
    with open(img, "wb") as f:
        subprocess.run(command, stdout=f)

    # Récupération de la zone de l'écran
    img = Image.open(img)
    width, height = img.size
    imCrop = img.crop((int(width * left), int(height * upper), int(width * right), int(height * bottom)))

    # Recherche de la chaîne de caractères
    reader = Reader(['fr'])
    ocrStringsFound = reader.readtext(imCrop, detail=0)
    if search_string in ocrStringsFound:
        return True

    # Suppression du fichier temporaire
    remove(".screenshot.png")

    return False
