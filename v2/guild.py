from subprocess import run
from time import sleep
from utils import tap_screen, swipe_screen

ADB_SERVER_PATH = r"D:\Program Files\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe"

def guilde_daily():
    tap_screen(1476, 589) # Clic sur le logo Guilde
    sleep(1)
    tap_screen(948, 678) # Clic sur le bouton Avis Confirmer
    sleep(12)
    tap_screen(837, 731) # Clic sur le bouton Recompense de guilde Confirmer
    sleep(1)
    tap_screen(948, 678) # Clic sur le bouton up
    sleep(1)
    swipe_screen(228, 546, 228, 546, 2000)
    tap_screen(1428, 731) # Clic sur le logo interaction
    sleep(1)