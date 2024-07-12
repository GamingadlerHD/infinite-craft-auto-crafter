import pyautogui
import time

class mouse_controll:
    def click(x, y):
        pyautogui.moveTo(x, y, 0)
        pyautogui.mouseDown()
        time.sleep(0.02)
        pyautogui.mouseUp()

    def dragItem(start_x, start_y, end_x, end_y, time):
        # Move to the starting position
        pyautogui.moveTo(start_x, start_y)
        # Perform the drag-and-drop action
        pyautogui.mouseDown()
        pyautogui.moveTo(end_x, end_y, duration=time)  # Duration is optional
        pyautogui.mouseUp()