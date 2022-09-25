import os
from PIL import Image
import easyocr
from adbutils import adb

def CurrentPage(deviceAddress="127.0.0.1:5555"):
    adb.connect(deviceAddress)
    adb.device(serial=deviceAddress).screenshot().save(".screencap.png")
    imCrop = Image.open(r".screencap.png").crop((0, 0, int((Image.open(".screencap.png").size[0])/5), int((Image.open(".screencap.png").size[1])/8)))
    imCrop.save(".screencap.png")
    ocrStringsFound = easyocr.Reader(['fr']).readtext(".screencap.png", detail=0)
    os.remove(".screencap.png")
    return (ocrStringsFound[0])