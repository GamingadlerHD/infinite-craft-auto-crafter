from Database.dbConection import DbConection
from utils.mouse import mouse_controll
from utils.keyboard import keyboard_controll
import time
import pyautogui
# import pytesseract
# from PIL import Image



def run():
    db = DbConection()

    print("Autocrafting started")

    for i in range(5, 0):
        time.sleep(1)
        print(f"{i}")

    for i in range(150, 160):
        item1, item2, result = db.get(i)
        toTextBox()
        keyboard_controll.typeText(item1)
        dragItem(1546, 97, 1150, 130)
        clearSearch()
        toTextBox()
        keyboard_controll.typeText(item2)
        dragItem(1546, 97, 1150, 130)
        time.sleep(0.05)
        print(f"Crafted {result}")
        clean()
        clearSearch()

# def screenshot(ltx, lty, rbx, rby):
#     width = rbx - ltx
#     height = rby - lty
#     return pyautogui.screenshot(region=(ltx, lty, width, height))

def toTextBox():
    mouse_controll.click(1612, 1124)

def clean():
    mouse_controll.click(1464, 1127)

def toItem():
    mouse_controll.click(1546, 97)

def toBoard():
    mouse_controll.click(900, 500)

def clearSearch():
    mouse_controll.click(1840, 1124)

def dragItem(start_x, start_y, end_x, end_y):
    # Move to the starting position
    pyautogui.moveTo(start_x, start_y)
    # Perform the drag-and-drop action
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=0.1)  # Duration is optional
    pyautogui.mouseUp()



# lt 1090 120
# rb 1444 260

    #scr = screenshot(1090, 120, 1444, 260).save("screenshot.png")
    #text = pytesseract.image_to_string("screenshot.png")
    #if text.toLower() != result.toLower():
    #    print(f"Error crafting {result}")
    #     continue
    # else:
    #     

print("Autocrafting finished")