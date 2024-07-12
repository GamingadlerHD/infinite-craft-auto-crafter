import time
import pyautogui

class keyboard_controll:
    def typeText(string):
        for char in string:
            pyautogui.keyDown(char)
            time.sleep(0.002)
            pyautogui.keyUp(char)
            time.sleep(0.002)

    def pasteText(string):
        pyautogui.hotkey('ctrl', 'v')