import os, time
from PIL import Image
import easyocr
from adbutils import adb

def ocrCropGetString(left: float, upper: float, right: float, bottom: float, deviceAddress="127.0.0.1:5555"):
    img = ".ocrCrop.png"
    adb.device(deviceAddress).screenshot().save(img)
    width, height = Image.open(img).size
    imCrop = Image.open(img).crop(
        (int(width * left), int(height * upper), int(width * right), int(height * bottom)))
    imCrop.save(img)
    ocrStringsFound = easyocr.Reader(['fr']).readtext(img, detail=0)
    os.remove(img)
    if ocrStringsFound != None:
        return (ocrStringsFound)
    elif ocrStringsFound == None:
        return ("No string found")
    else:
        return ("Error: ocrCropGetString fonction")

def AdbClick(x, y, deviceAddress="127.0.0.1:5555"):
    if x != 0 and y !=0:
        img = ".ocrCrop.png"
        adb.connect(deviceAddress)
        adb.device(deviceAddress).screenshot().save(img)
        width, height = Image.open(img).size
        os.remove(img)
        adb.device(deviceAddress).click(float((x * width) / 100), float((y * height) / 100))
        return ()
    else:
        return (print("Error this function need coordinates"))

def AdbClickString(string):
    if AdbFindStringLocation(string) != False:
        x, y = AdbFindStringLocation(string)
        AdbClick(x, y)
        return (print(f"Tap in {x, y}"))
    else:
        return (False)

def AdbSwipe(x, y, duration, deviceAddress="127.0.0.1:5555"):
    if x != 0 and y !=0:
        img = ".ocrCrop.png"
        adb.connect(deviceAddress)
        adb.device(deviceAddress).screenshot().save(img)
        width, height = Image.open(img).size
        os.remove(img)
        adb.device(deviceAddress).swipe(float((x * width) / 100), float((y * height) / 100), (x * width) / 100, float((y * height) / 100), duration)
        return (print(f"Tap in {x, y} for {duration}s"))
    else:
        return (print("Error this function need coordinates"))

def AdbFindStringLocation(string, deviceAddress="127.0.0.1:5555"):
    img = ".screencap.png"
    adb.device(deviceAddress).screenshot().save(img)
    width, height = Image.open(img).size
    stringsFound = easyocr.Reader(['fr']).readtext(img)
    strMatchList = []
    print(stringsFound)
    for i in range(0, len(stringsFound)):
        if stringsFound[i][1] == string:
            strMatchList.append(stringsFound[i][0][0])
    os.remove(img)
    if len(strMatchList) == 0:
        return (False)
    elif len(strMatchList) > 0:
        x, y = strMatchList[0]
        x = float((x * 100) / width)
        y = float((y * 100) / height)
        return (x, y)

def EvenConfimePopUp():
    AdbClickString("Confirmer")
    return ()

def PopUp(YesOrNo: bool):
    if YesOrNo == True:
        AdbClick(58, 79)
        return ()
    elif YesOrNo == False:
        AdbClick(41, 79)
        return ()
    else:
        return (print("error"))

def CollectFarm():
    print("E")