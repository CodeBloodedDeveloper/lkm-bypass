import pyautogui
import time

time.sleep(7)
with open('code.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        time.sleep(0.1)
        pyautogui.write(line.lstrip().rstrip() + '\n')  
