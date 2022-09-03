import pyautogui
import time

time.sleep(3)
# range will be the number of TikTok's
for i in range(10):
    pyautogui.moveTo(450, 500)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.moveTo(854, 515)
    time.sleep(1)
    pyautogui.leftClick()