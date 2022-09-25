import os
import time

import model.CommonWorkflow
from PIL import Image
import easyocr
from adbutils import adb

deviceAddress = "127.0.0.1:5555"
buttonBattleOpponent1 = 88, 45
buttonSwapOpponent1 = 94, 31
buttonSwapOpponent2 = 94, 60
buttonBattleOpponent2 = 88, 74
buttonBattleStart = 76, 89
buttonBattleCancel = 49, 89
buttonEndBattleConfirmRank = 50, 75
buttonEndBattleConfirm = 50, 89


def ocrCropGetString(left: float, upper: float, right: float, bottom: float, deviceAddress: str = '127.0.0.1:5555'):
    img = ".ocrCrop.png"
    adb.connect(deviceAddress)
    adb.device(serial=deviceAddress).screenshot().save(img)
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
def click(button):
    x, y = button[0], button[1]
    print(x, y)
    if x != 0 and y !=0:
        img = ".ocrCrop.png"
        adb.connect(deviceAddress)
        adb.device(serial=deviceAddress).screenshot().save(img)
        width, height = Image.open(img).size
        os.remove(img)
        adb.device(serial=deviceAddress).click(float((x * width) / 100), float((y * height) / 100))
        return ()
    else:
        return (print("Error this function need coordinates"))

def battle():
    click(buttonSwapOpponent1)
    click(buttonSwapOpponent2)

    if Opponent1.Toughness > Opponent2.Toughness:
        click(buttonBattleOpponent1)

    else:
        click(buttonBattleOpponent2)

    time.sleep(2)
    click(buttonBattleStart)
    time.sleep(60)
    for i in range(2):
        click(buttonEndBattleConfirmRank)
        time.sleep(2)
        click(buttonEndBattleConfirm)
        time.sleep(8)
class Opponent1:
    ocrStringsFound = ocrCropGetString(0.62, 0.37, 0.82, 0.54)
    DPS, Toughness = ocrStringsFound[1], ocrStringsFound[3]
class Opponent2:
    ocrStringsFound = ocrCropGetString(0.62, 0.66, 0.82, 0.84)
    DPS, Toughness = ocrStringsFound[1], ocrStringsFound[-1]
class Tickets:
        ocrStringsFound = ocrCropGetString(0.64, 0.87, 0.82, 0.94)
        remainingTicket = ocrStringsFound[0][0]
        nextTicketTime = ocrStringsFound[-1]

if model.CommonWorkflow.CurrentPage() != "Colisée":
    print("Error i work only in colosseum")
    exit()

elif int(Tickets.remainingTicket) < 1:
    print("No ticket found")
    exit()

battle()
