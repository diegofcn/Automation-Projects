# Import relevant modules
import pyautogui
import time

# Give the python time somme time before continuing
time.sleep(3)

# Mouse Functions

# prints resolution of the screen
print(pyautogui.size())
# prints the current position of the cursor
print(pyautogui.position())
# Moves the mouse over time (3 seconds)
pyautogui.moveTo(100, 100, 3)
# Move the mouse relative to its current position
pyautogui.moveRel(100, 100, 3)

# Click
pyautogui.click(500, 500, 3, 3, button="left")
# pyautogui.doubleClick
# pyautogui.leftClick
# pyautogui.rightClick
# pyautogui.tripleClick

# scrolls up
pyautogui.scroll(500)

# scrolls down
pyautogui.scroll(-500)

# Mouse up and down
pyautogui.mouseUp(100, 100, button="left")
pyautogui.mouseDown(100, 100, button="left")

# example of Mouse up and down (Paint)
pyautogui.mouseUp(300, 300, button="left")
pyautogui.moveTo(800, 400, 3)
pyautogui.mouseUp()
pyautogui.moveTo(1000, 400, 3)

# Keyboard Functions
pyautogui.write("hello")
pyautogui.press("enter")
pyautogui.press("space")

# Screenshot
pyautogui.screenshot("screenshot.png")