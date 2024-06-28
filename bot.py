from dbConection import DbConection
import win32api, win32con
import time
import pyautogui
import pytesseract
from PIL import Image


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def screenshot(ltx, lty, rbx, rby):
    width = rbx - ltx
    height = rby - lty
    return pyautogui.screenshot(region=(ltx, lty, width, height))

def toTextBox():
    click(1612, 1124)

def clean():
    click(1464, 1127)

def toItem():
    click(1546, 97)

def toBoard():
    click(900, 500)

def clearSearch():
    click(1840, 1124)

def typeText(string):
    for char in string:
        pyautogui.keyDown(char)
        # time.sleep(0.002)
        pyautogui.keyUp(char)
        # time.sleep(0.002)

def dragItem(start_x, start_y, end_x, end_y):
    # Move to the starting position
    pyautogui.moveTo(start_x, start_y)
    # Perform the drag-and-drop action
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=0.1)  # Duration is optional
    pyautogui.mouseUp()

db = DbConection()
print("Autocrafting started")
time.sleep(5)
for i in range(150, 200):
    item1, item2, result = db.get(i)
    toTextBox()
    typeText(item1)
    dragItem(1546, 97, 1150, 130)
    clearSearch()
    toTextBox()
    typeText(item2)
    dragItem(1546, 97, 1150, 130)
    time.sleep(0.05)


# lt 1090 120
# rb 1444 260

    #scr = screenshot(1090, 120, 1444, 260).save("screenshot.png")
    #text = pytesseract.image_to_string("screenshot.png")
    #if text.toLower() != result.toLower():
    #    print(f"Error crafting {result}")
    #     continue
    # else:
    #     print(f"Crafted {result}")
    # clean()
    # clearSearch()

print("Autocrafting finished")