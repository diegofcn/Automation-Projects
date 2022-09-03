import pyautogui
import time


def SendMessage():
    time.sleep(4)
    text = open('message.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press("enter")


SendMessage()