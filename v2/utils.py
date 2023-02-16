from subprocess import run
from time import sleep
from easyocr import Reader
from PIL import Image

ADB_SERVER_PATH = r"D:\Program Files\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe"

def tap_screen(x, y):
    command = [ADB_SERVER_PATH, "shell", "input", "tap", str(x), str(y)]
    run(command)

def swipe_screen(start_x, start_y, end_x, end_y, duration):
    command = [ADB_SERVER_PATH, "shell", "input", "swipe", str(start_x), str(start_y), str(end_x), str(end_y), str(duration)]
    run(command)