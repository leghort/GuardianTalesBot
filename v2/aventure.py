from subprocess import run
from time import sleep

ADB_SERVER_PATH = r"D:\Program Files\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe"

def tap_screen(x, y):
    command = [ADB_SERVER_PATH, "shell", "input", "tap", str(x), str(y)]
    run(command)

def aventure_daily():
    tap_screen(115, 770)  # Clic sur le bouton Aventure
    sleep(1)
    tap_screen(80, 300)  # Clic sur le bouton Faille
    sleep(1)
    tap_screen(481, 668)  # Clic Donjon d'éveil
    sleep(1)
    tap_screen(1482, 804)  # Clic sur le bouton auto-repetition
    sleep(1)
    for i in range(2):
        tap_screen(1087, 454) # Clic sur le bouton plus
        sleep(1)
    tap_screen(1051, 700)  # Clic sur le bouton Avance rapide
    sleep(20)
    tap_screen(801, 746)  # Clic sur le bouton Confirmer avance rapide
    sleep(1)
    tap_screen(801, 672)  # Clic sur le bouton Confirmer point event
    sleep(1)
    for i in range(3):
        tap_screen(40, 40) # Clic sur le bouton Retour
        sleep(1)