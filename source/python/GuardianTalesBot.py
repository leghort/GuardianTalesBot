from homeWorkflow import getDailyShop
from adventureWorkflow import getDailyDonjon

dailyShop = False
dailyDongeon = False
dailyGuild = False
dailyEvent = False
dailyFarm = False

if dailyShop != True:
    print("getDailyShop")
    getDailyShop()
    dailyShop == True

if dailyDongeon != True:
    print("getDailyDonjon")
    getDailyDonjon()
    dailyDongeon == True