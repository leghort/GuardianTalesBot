import os
import time
import psutil
import easyocr
from adbutils import adb

deviceAddress = "127.0.0.1:5555"
def get_pid(processName):
    for i in psutil.process_iter():
        if processName in i.name():
            processPid = i.pid
    return processPid
def shell_adb(deviceAddress, commande):
    adb.connect(deviceAddress)
    return (adb.device(serial=deviceAddress).shell(commande))
def adb_find_app(deviceAddress, app):
    appFound = 0
    for i in range(0, len(adb.device(serial=deviceAddress).list_packages())):
        if adb.device(serial=deviceAddress).list_packages()[i] == app:
            appFound = 1
    return appFound
def adb_tap_string(string):
    time.sleep(1)
    adb.connect(deviceAddress)
    adb.device(serial=deviceAddress).shell("screencap -p /sdcard/.screencap.png")
    adb.device(serial=deviceAddress).sync.pull("/sdcard/.screencap.png", ".screencap.png")
    adb_tap_string.reader = easyocr.Reader(['fr']).readtext(".screencap.png")
    strMatchList = []
    for i in range(0, len(adb_tap_string.reader)):
        if adb_tap_string.reader[i][1] == string:
            strMatchList.append(adb_tap_string.reader[i][0][0])
    os.remove(".screencap.png")
    stringCordonate = strMatchList[0]
    adb.device(serial=deviceAddress).click(stringCordonate[0], stringCordonate[1])
    return ()

def collisee_V2():
    adb_tap_string("Aventure")
    time.sleep(4)
    adb_tap_string("Colisée")
    time.sleep(4)
    adb_tap_string("Début bataille")
    time.sleep(4)
    adb_tap_string("Début bataille")
    time.sleep(60)
    adb_tap_string("Confirmer")
    time.sleep(4)
    adb_tap_string("Confirmer")
    time.sleep(2)
    adb.device(serial=deviceAddress).click(50, 50)
    time.sleep(2)
    adb.device(serial=deviceAddress).click(50, 50)




def guilde_V1():
    adb_tap_string("Guilde")
    time.sleep(2)
    adb_tap_string("Confirmer")
    time.sleep(4)
    adb.device(serial=deviceAddress).swipe(287, 724, 282, 620, 0.5)
    time.sleep(2)
    adb.device(serial=deviceAddress).click(1724, 880)
    time.sleep(2)
    adb_tap_string("Recevoir")
    time.sleep(2)
    adb_tap_string("Confirmer")
    time.sleep(2)
    adb.device(serial=deviceAddress).click(1862, 50)
    time.sleep(1)
    adb.device(serial=deviceAddress).click(1862, 50)
    time.sleep(2)
    adb_tap_string("Confirmer")
    return ()

def dailyV1():
    guilde_V1()
    time.sleep(2)
    donjon()
    donjon()
    donjon()
    getQuestReword()


def getQuestReword():
    adb.device(serial=deviceAddress).click(575, 969)
    time.sleep(1)
    list = ["Quotidienne", "Défi", "Événement"]
    for i in range (0, (len(list))):
        adb_tap_string(list[i])
        adb_tap_string("Tout recevoir")

    time.sleep(1)
    adb.device(serial=deviceAddress).click(50, 50)

def donjon():
    adb_tap_string("Aventure")
    adb_tap_string("Faille")
    adb_tap_string("Donjon d'éveil")
    time.sleep(2)
    adb.device(serial=deviceAddress).click(1389, 964)
    time.sleep(60)
    adb_tap_string("Sortie")
    time.sleep(8)
    adb_tap_string("Confirmer")
    adb.device(serial=deviceAddress).click(50, 50)
    time.sleep(2)
    adb.device(serial=deviceAddress).click(50, 50)
    time.sleep(2)
    adb.device(serial=deviceAddress).click(50, 50)
    time.sleep(2)


loop = "true"
while loop == "true":
    collisee_V2()
    time.sleep(7200)
