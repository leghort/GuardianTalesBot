from subprocess import run
from time import sleep


ADB_SERVER_PATH = r"C:\Program Files\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe"
APP_PACKAGE = "com.kakaogames.gdts"

def stop_app():
    command = [ADB_SERVER_PATH, "shell", "am", "force-stop", APP_PACKAGE]
    run(command)

def stop_guardian_tales():
    stop_app()
    sleep(2)
