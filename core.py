from Database.dbConection import DbConection
from utils.CraftTools import craftItem
from utils.keyboard import keyboard_controll
import time
import os
import json
from pyautogui import displayMousePosition
from colorama import Fore, Style
# import pytesseract
# from PIL import Image



def run():
    # select mode
    Modes = ["Database", "Display", "Create Collection", "Load Collection", "One to Collection", "Converter", "Add to Collection"]
    awnser = ""

    while awnser not in Modes:
        print("Modes: Database, Create Collection, Load Collection, Add to Collection, One to Collection, Converter, Display")
        awnser = input("Select mode: ")

    match awnser:
        case "Database":
            runFromDatabase()
        case "Load Collection":
            runFromArray()
        case "Add to Collection":
            addToArray()
        case "Create Collection":
            createArray()
        case "Display":
            displayMousePosition()
        case "One to Collection":
            oneToCollection()
        case "Converter":
            converter()
        

def runFromDatabase():
    db = DbConection()

    start = int(input("Enter start number: "))
    stop = int(input("Enter stop number: "))

    print("Autocrafting started")

    for i in range(0, 5):
        time.sleep(1)
        print(f"{i}/5")

    for i in range(start, stop):
        if keyboard_controll.keyPressed('x'):
            break
        item1, item2, result = db.get(i)
        sucess = craftItem(item1, item2)
        if sucess != False:
            print(Fore.LIGHTBLUE_EX + f"Crafted {result}")
        else:
            print(Fore.LIGHTYELLOW_EX + f"Failed to craft {result}")

    print(Fore.LIGHTGREEN_EX + "Autocrafting finished")

def createArray():
    items = []
    os.makedirs("saves", exist_ok=True)
    
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
            if keyboard_controll.keyPressed('x'):
                break
            item2 = items[e]
            sucess = craftItem(item, item2)
            if sucess != False:
                print(Fore.LIGHTBLUE_EX + f"Crafted")
            else:
                print(Fore.LIGHTYELLOW_EX + f"Failed to craft")

def converter():
    name = input("Enter the name of the collection: ")
    with open(f'saves/{name}.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    elements = [element['text'] for element in data['elements']]

    newName = input("Enter the new name: ")

    with open(f'saves/{newName}.json', 'w') as file:
        json.dump(elements, file)

def oneToCollection():
    name = input("Enter the name of the collection: ")
    item2 = input("Enter the item to craft with: ")
    with open(f'saves/{name}.json', 'r') as file:
        items = json.load(file)
    for i in range(0, (len(items) -1)):
        if keyboard_controll.keyPressed('x'):
            break
        item = items[i]
        sucess = craftItem(item, item2, ((i % 6)-3))
        if sucess != False:
            print(Fore.LIGHTBLUE_EX + f"Crafted")
        else:
            print(Fore.LIGHTYELLOW_EX + f"Failed to craft")
            