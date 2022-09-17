import psutil
import easyocr
from adbutils import adb

# Get the precess id by process name
def get_pid(processName):
    for i in psutil.process_iter():
        if processName in i.name():
            pid = i.pid
    return pid

# Connect a device by adb and seen commande
def shell_adb(deviceAddress, commande):
    adb.connect(deviceAddress)
    return (adb.device(serial=deviceAddress).shell(commande))

# Find text in picture
def ocr(file, string):
    reader = easyocr.Reader(['fr'])
    result = reader.readtext(file)
    str_match = list(filter(lambda x: string in x, result))
    return str_match


#print (get_pid("HD-Player"))
#print (shell_adb("127.0.0.1:5555","ls"))
print (ocr("screencap1.png","DPS"))