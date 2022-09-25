import os
import time
import psutil
import easyocr
from adbutils import adb

import model.Achievements
import model.ColosseumPage
import model.HomePage
import model.RiftPage
import model.WorldMapPage
import model.CommonWorkflow

Common = model.CommonWorkflow
Achievements= model.Achievements
ColosseumPage= model.ColosseumPage
HomePage= model.HomePage
RiftPage= model.RiftPage
WorldMapPage= model.WorldMapPage

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
    return
def adb_find_string(string):
    time.sleep(1)
    adb.connect(deviceAddress)
    adb.device(serial=deviceAddress).screenshot().save(".screencap.png")
    adb_tap_string.reader = easyocr.Reader(['fr']).readtext(".screencap.png")
    strMatchList = []
    for i in range(0, len(adb_tap_string.reader)):
        if adb_tap_string.reader[i][1] == string:
            strMatchList.append(adb_tap_string.reader[i][0][0])
    os.remove(".screencap.png")
    if len(strMatchList) == 0:
        return (False)
    elif len(strMatchList) > 0:
        return (True)
def adb_tap_string(string):
    time.sleep(1)
    adb.connect(deviceAddress)
    adb.device(serial=deviceAddress).screenshot().save(".screencap.png")
    adb_tap_string.reader = easyocr.Reader(['fr']).readtext(".screencap.png")
    strMatchList = []
    for i in range(0, len(adb_tap_string.reader)):
        if adb_tap_string.reader[i][1] == string:
            strMatchList.append(adb_tap_string.reader[i][0][0])
    os.remove(".screencap.png")
    if len(strMatchList) == 0:
        return ()
    elif len(strMatchList) > 0:
        stringCordonate = strMatchList[0]
        adb.device(serial=deviceAddress).click(stringCordonate[0], stringCordonate[1])
        return (stringCordonate)
def adb_tap(coordinates=[0,0]):
    if coordinates != [0,0]:
        adb.device(serial=deviceAddress).click(coordinates[0], coordinates[1])
        return (coordinates)
    else:
        return (print("Error this function need coordinates"))
def guilde_V1():
    adb_tap_string("Guilde")
    time.sleep(2)
    adb_tap_string("Confirmer")
    time.sleep(9)
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
def getQuestReword():
    adb.device(serial=deviceAddress).click(575, 969)
    time.sleep(1)
    list = ["Quotidienne", "Défi", "Événement"]
    for i in range (0, (len(list))):
        adb_tap_string(list[i])
        adb_tap_string("Tout recevoir")
        time.sleep(2)
        adb_tap_string("Confirmer")
    time.sleep(1)
    adb.device(serial=deviceAddress).click(50, 50)

def donjon():
    loop = True
    stringsList = ["Aventure", "Faille", "Donjon d'éveil"]
    for string in stringsList:
        adb_tap_string(string)
        time.sleep(2)
    while loop == True:
        if adb_find_string("Recharger ticket") == True:
            loop = False
        elif adb_find_string("Recharger ticket") == False:
                adb.device(serial=deviceAddress).click(1389, 964)
                time.sleep(60)
                adb_tap_string("Sortie")
                time.sleep(8)
                adb_tap_string("Confirmer")
                time.sleep(4)
        else:
            loop = False
            print("function donjon error")
    for i in range(3):
        adb.device(serial=deviceAddress).click(50, 50)
        time.sleep(2)


def shop():
    adb_tap_string("Menu")
    time.sleep(4)
    adb_tap([909, 430])
    time.sleep(4)
    stringsList = ["Ressource", "Gratuit", "Gratuit", "Confirmer", "Équipement", "Marteau consolidateur"]
    for string in stringsList:
        adb_tap_string(string)
        time.sleep(4)
    adb.device(serial=deviceAddress).click(1132, 858)
    time.sleep(2)
    adb_tap_string("Confirmer")
    time.sleep(2)
    adb.device(serial=deviceAddress).click(50, 50)
    time.sleep(2)
    adb.device(serial=deviceAddress).click(630, 443)
    time.sleep(2)

def dailymsg():
    for i in range(2):
        if len(adb_tap_string("Recevoir récompense")) > 0:
            adb_tap_string("Recevoir récompense")
            if len(adb_tap_string("Confirmer")) > 0:
                adb_tap_string("Confirmer")
        elif len(adb_tap_string("Recevoir récompenses")) > 0:
            adb_tap_string("Recevoir récompenses")
            if len(adb_tap_string("Confirmer")) > 0:
                adb_tap_string("Confirmer")
def collisee_V2():
    adb_tap_string("Aventure")
    time.sleep(4)
    if len(adb_tap_string("Colisée")) > 0:
        adb_tap_string("Colisée")
        time.sleep(4)
    adb_tap([1718,478])
    time.sleep(2)
    adb_tap_string("Début bataille")
    if len(adb_tap_string("Confirmer")) > 0:
        adb_tap_string("Confirmer")
        time.sleep(4)
        adb_tap_string("Confirmer")
def daily_V2():
    shop()
    time.sleep(4)
    guilde_V1()
    time.sleep(4)
    for i in range(3):
        donjon()
    getQuestReword()

print(ColosseumPage.opponent1())