import subprocess
import time


ADB_SERVER_PATH = r"D:\Program Files\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe"
APP_PACKAGE = "com.kakaogames.gdts"

def stop_app():
    command = [ADB_SERVER_PATH, "shell", "am", "force-stop", APP_PACKAGE]
    subprocess.run(command)

def stop_guardian_tales():
    stop_app()
    time.sleep(2)
