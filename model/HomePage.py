from adbutils import adb

buttonGuardianAvatar = [50, 50]
buttonStamina = [860, 50]
buttonGoldCoins = [1150, 50]
buttonGem = [1430, 50]
buttonAchivements = [580, 970]
buttonEvent = [1640, 260]
buttonHero = [150, 700]
buttonAventure = [150, 900]
buttonGuilde = [1777, 700]
buttonSummons = [1777, 900]
buttonMenu = [1820, 440]
buttonMenuReduce = [632, 440]

class Menu:
    buttonForum = [766, 440]
    buttonShop = [909, 440]
    buttonQuest = [1055, 440]
    buttonBook = [1199, 440]
    buttonInventory = [1340, 440]
    buttonAttendance = [1490, 440]
    buttonEnhance = [1633, 440]
    buttonSNS = [1771, 440]
    class Attendance:
        buttonClose = [957, 930]
        buttonCloseEvent = [960, 790]
class Guilde:
    buttonCancel = [800, 800]
    buttonConfirm = [1120, 800]

def clickAdventureButton(deviceAddress="127.0.0.1:5555"):
    adb.device(serial=deviceAddress).click(buttonAventure[0], buttonAventure[1])