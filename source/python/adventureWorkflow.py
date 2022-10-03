import time
from commonWorkflow import AdbFindStringLocation, AdbClick, ocrCropGetString, EvenConfimePopUp

def getDailyDonjon():
    # Aller dans le menu dongon
    strinList = ["Aventure", "Faille", "Donjon d'éveil", "Auto-répétit?"]
    for i in strinList:
        if AdbFindStringLocation(i) != False:
            x, y = AdbFindStringLocation(i)
            AdbClick(x, y)
            time.sleep(2)
        else:
            return (print("String not found"))
    # Définit le nombre de repetition gratuit
    loop = True
    while loop == True:
        time.sleep(1)
        gemmesRequire = ocrCropGetString(0.39, 0.63, 0.50, 0.70)[-1]
        if int(gemmesRequire) == 0:
            AdbClick(67, 49)
            time.sleep(1)
            gemmesRequire = ocrCropGetString(0.39, 0.63, 0.50, 0.70)[-1]
            if int(gemmesRequire) == 300:
                AdbClick(32, 49)
                loop = False
        elif int(gemmesRequire) >= 300:
            AdbClick(32, 49)
        else:
            return (print("Error try not found"))
    # Lance le combat
    strinList = ["Avance rapide", "Confirmer"]
    for i in strinList:
        if AdbFindStringLocation(i) != False:
            x, y = AdbFindStringLocation(i)
            AdbClick(x, y)
            time.sleep(4)
        else:
            return (print("String not found"))
    EvenConfimePopUp()
    # Retour au menu
    for i in range(3):
        time.sleep(1)
        AdbClick(2, 4)
    return ()





