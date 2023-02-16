import time
from commonWorkflow import AdbFindStringLocation, AdbClick, PopUp, AdbSwipe, AdbClickString
from adbutils import adb

def getDailyGuild():
    AdbClickString("Guilde")
    PopUp(True)
    time.sleep(8)
    AdbSwipe(10, 64, 0.5)
    AdbClick(89, 81)
    time.sleep(2)
    strinList = ["Recevoir", "Confirmer"]
    for i in strinList:
        if AdbFindStringLocation(i) != False:
            x, y = AdbFindStringLocation(i)
            AdbClick(x, y)
            time.sleep(2)
        else:
            return (print("String not found"))
    AdbClick(94, 17)
    time.sleep(1)
    AdbClick(96, 4)
    PopUp(True)