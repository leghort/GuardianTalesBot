import time
from adbutils import adb
from commonWorkflow import AdbClick, AdbClickString, AdbFindStringLocation, PopUp

def getDailyShop():
    listString = ["Menu", "Boutique", "Ressource", "Gratuit"]
    for string in listString:
        time.sleep(2)
        x, y = AdbFindStringLocation(string)
        x = x + 2
        AdbClick(x, y)
    time.sleep(1)
    PopUp(True)
    time.sleep(1)
    AdbClickString("Confirmer")
    listString = ["Équipement", "Marteau consolidateur"]
    for string in listString:
        time.sleep(2)
        x, y = AdbFindStringLocation(string)
        AdbClick(x, y)
    time.sleep(1)
    PopUp(True)
    time.sleep(1)
    AdbClickString("Confirmer")
    time.sleep(1)
    AdbClick(2, 4)
    time.sleep(2)
    AdbClick(32, 40)
    return ()

def getQuestReward():
    adb.device.click(575, 969)
    time.sleep(1)
    list = ["Quotidienne", "Défi", "Événement"]
    for i in range (0, (len(list))):
        AdbClickString(list[i])
        AdbClickString("Tout recevoir")
        time.sleep(2)
        AdbClickString("Confirmer")
    time.sleep(1)
    adb.device.click(50, 50)
