from subprocess import run
from time import sleep

ADB_SERVER_PATH = r"D:\Program Files\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe"

def tap_screen(x, y):
    command = [ADB_SERVER_PATH, "shell", "input", "tap", str(x), str(y)]
    run(command)

def shop_menu():
    tap_screen(1016, 40) # Clic sur le logo Piece en or
    sleep(1)
    tap_screen(40, 40) # Clic sur le bouton Retour
    sleep(1)

def shop_daily():
    tap_screen(1016, 40) # Clic sur le logo Piece en or
    sleep(1)
    tap_screen(815, 383) # Clic sur le bouton Ressouce Or
    sleep(1)
    tap_screen(997, 731) # Clic sur le bouton Achat
    sleep(1)
    tap_screen(800, 667) # Clic sur le bouton Confirmer
    sleep(1)
    tap_screen(173, 500) # Clic sur le menu Equipement
    sleep(1)
    tap_screen(512, 364) # Clic sur le bouton Marteau consolidateur
    sleep(1)
    tap_screen(997, 731) # Clic sur le bouton Achat
    sleep(1)
    tap_screen(800, 667) # Clic sur le bouton Confirmer
    sleep(1)
    tap_screen(40, 40) # Clic sur le bouton Retour
    sleep(1)