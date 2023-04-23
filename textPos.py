

import random
import time
import pyautogui


print(random.randrange(1,3))
# time.sleep(3)
# # print(pyautogui.position())
img_capture = pyautogui.locateOnScreen("capBtn.png")
print(img_capture)
print(img_capture)
pyautogui.keyDown(img_capture)