import psutil
from adbutils import adb

def get_pid(processName):
    processName = processName
    pid = None

    for proc in psutil.process_iter():
        if processName in proc.name():
            pid = proc.pid
    return pid

print(get_pid("HD-Player"))

adb.connect("127.0.0.1:5555")
adndevies = adb.device_list()
print(adb.device(serial="127.0.0.1:5555").shell("help -a"))