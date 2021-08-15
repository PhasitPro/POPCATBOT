import pyautogui as py
import time
import keyboard as kb


py.hotkey('win')
py.write('Google', interval=0.01)
time.sleep(1)
py.typewrite(['enter'])
time.sleep(1)
py.write('https://popcat.click/', interval=0.01)
py.typewrite(['enter'])

numClick = 1000
for i in range(numClick):
    py.hotkey('ctrl')
    time.sleep(0.00001)
