import pyautogui
import time
import pyscreeze
# #保护措施，避免失控
# pyautogui.FAILSAFE = True
# #为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。
# pyautogui.PAUSE = 0.5


#time.sleep(3)
'''
location = pyautogui.locateCenterOnScreen('baozang.png',confidence = 0.8)

print(location)

# 获取当前屏幕分辨率
743 242
618 679
1158 811
1299 331
'''
#1435 810
screenWidth, screenHeight = pyautogui.size()
print(screenWidth,screenHeight)
# 获取当前鼠标位置
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX,currentMouseY)

