from Database.dbConection import DbConection
from utils.CraftTools import craftItem
import time
import json
from pyautogui import displayMousePosition
from colorama import Fore, Style
# import pytesseract
# from PIL import Image



def run():
    # select mode
    Modes = ["Database", "Display", "ca", "la", "aa"]
    aw = ""

    while aw not in Modes:
        print("Modes: Database, ca, la, aa, Display")
        aw = input("Select mode: ")

    if aw == "Database": 
        runFromDatabase()
    elif aw == "la":
        runFromArray()
    elif aw == "aa":
        addToArray()
    elif aw == "ca":
        createArray()
    elif aw == "Display":
        displayMousePosition()

def runFromDatabase():
    db = DbConection()

    print("Autocrafting started")

    for i in range(0, 5):
        time.sleep(1)
        print(f"{i}/5")

    for i in range(150, 155):
        item1, item2, result = db.get(i)
        sucess = craftItem(item1, item2)
        if sucess != False:
            print(Fore.LIGHTBLUE_EX + f"Crafted {result}")
        else:
            print(Fore.LIGHTYELLOW_EX + f"Failed to craft {result}")

    print(Fore.LIGHTGREEN_EX + "Autocrafting finished")

def createArray():
    items = []
    
    while True:
        item = input("Enter an item, or start crafting by pressing enter: ")
        if item == "":
            break
        items.append(item)
    
    name = input("Enter the name of the collection: ")
    open(f'saves/{name}.json', 'w').close()
    with open(f'saves/{name}.json', 'w') as file:
        json.dump(items, file)
    
def addToArray():
    name = input("Enter the name of the collection: ")
    with open(f'saves/{name}.json', 'r') as file:
        items = json.load(file)
    
    while True:
        item = input("Enter an item, or start crafting by pressing enter: ")
        if item == "":
            break
        items.append(item)
    
    with open(f'saves/{name}.json', 'w') as file:
        json.dump(items, file)

def runFromArray():
    name = input("Enter the name of the collection: ")
    with open(f'saves/{name}.json', 'r') as file:
        items = json.load(file)
    for i in range(0, (len(items) -1)):
        item = items[i]
        for e in range (1+i, len(items)):
            item2 = items[e]
            sucess = craftItem(item, item2)
            if sucess != False:
                print(Fore.LIGHTBLUE_EX + f"Crafted")
            else:
                print(Fore.LIGHTYELLOW_EX + f"Failed to craft")