import subprocess
import time

ADB_SERVER_PATH = r"D:\Program Files\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe"
APP_PACKAGE = "com.kakaogames.gdts"

def connect_to_emulator():
    command = [ADB_SERVER_PATH, "connect", "localhost:7555"]
    subprocess.run(command)

def launch_app():
    command = [ADB_SERVER_PATH, "shell", "monkey", "-p", APP_PACKAGE, "1"]
    subprocess.run(command)

def stop_app():
    command = [ADB_SERVER_PATH, "shell", "am", "force-stop", APP_PACKAGE]
    subprocess.run(command)

def check_app_running():
    command = [ADB_SERVER_PATH, "shell", "pidof", APP_PACKAGE]
    result = subprocess.run(command, capture_output=True)
    return bool(result.stdout)

def tap_screen(x, y):
    command = [ADB_SERVER_PATH, "shell", "input", "tap", str(x), str(y)]
    subprocess.run(command)

def launch_guardian_tales():
    if check_app_running():
        print("Guardian Tales is already running!")
        return

    connect_to_emulator()
    launch_app()
    time.sleep(60)
    tap_screen(500, 800)