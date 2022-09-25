import os
import CommonWorkflow
from PIL import Image
import easyocr
from adbutils import adb

deviceAddress = "127.0.0.1:5555"

buttonBack = [50, 50]
buttonStamina = [860, 50]
buttonGoldCoins = [1150, 50]
buttonGem = [1430, 50]

buttonShop = [120, 370]
buttonReward = [120, 565]
buttonRanking = [120, 762]
buttonBattleRecord = [120, 950]

buttonBattleStartPlayer1 = [1700, 490]
buttonBattleStartPlayer2 = [1700, 800]
buttonSwapPlayers = [1836, 976]
buttonSwapPlayer1 = [1808, 334]
buttonSwapPlayer2 = [1808, 655]

buttonConfirmGetEventPoints = [969, 811]

class BattleStart:
    buttonBattleStart = [1200, 962]
    buttonCancel = [780, 962]
class BattleResul:
    buttonConfirm = [965, 969]
class SwapPlayers:
    buttonSwapPlayersConfim = [1131, 815]
    buttonSwapPlayersCancel = [812, 815]
def opponent1():
    img = ".opponent1.png"
    adb.connect(deviceAddress)
    adb.device(serial=deviceAddress).screenshot().save(img)
    width, height = Image.open(img).size
    imCrop = Image.open(img).crop(
        (int(width * 0.62), int(height * 0.37), int(width * 0.82), int(height * 0.54)))
    imCrop.save(img)
    ocrStringsFound = easyocr.Reader(['fr']).readtext(img, detail=0)
    os.remove(img)
    return (ocrStringsFound)

def opponent2():
    img = ".opponent2.png"
    adb.connect(deviceAddress)
    adb.device(serial=deviceAddress).screenshot().save(img)
    width, height = Image.open(img).size
    imCrop = Image.open(img).crop(
        (int(width * 0.62), int(height * 0.66), int(width * 0.82), int(height * 0.84)))
    imCrop.save(img)
    ocrStringsFound = easyocr.Reader(['fr']).readtext(img, detail=0)
    os.remove(img)
    return (ocrStringsFound)

if CommonWorkflow.CurrentPage() != "Colisée":
    print("Error i work only in colosseum")
    exit()

print(opponent1())
print(opponent2())