from utils.mouse import mouse_controll
from utils.keyboard import keyboard_controll
from bot_settings import settings
import pyperclip
from pyautogui import pixel
import time

def toTextBox():
    mouse_controll.click(settings.search_x, settings.search_y)

def clearSearch():
    mouse_controll.click(settings.clean_search_x, settings.clean_search_y)

def clean():
    mouse_controll.click(settings.clean_x, settings.clean_y)

def dragItemToBoard(time=0.15):
    mouse_controll.dragItem(settings.item_x, settings.item_y, settings.board_x, settings.board_y, time)

def enterText(string):
    pyperclip.copy(string)
    keyboard_controll.pasteText("")

def checkItemExists():
    rgb = pixel(1664, 113)
    return rgb != (0, 0, 0)

def getItem(item):
    clearSearch()
    toTextBox()
    enterText(item)
    if checkItemExists():
        dragItemToBoard()
        return True
    else:
        return False
        

def craftItem(item1, item2):
    ex = True

    ex = getItem(item1)

    if not ex:
        clean()
        return False
    
    time.sleep(0.05)

    ex = getItem(item2)

    clean()

    if not ex:
        return False