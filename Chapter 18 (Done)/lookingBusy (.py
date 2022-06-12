#! python3
# lookingBusy.py - nudges the mouse slightly every 10 seconds

import pyautogui, time
print('CTRL-C TO STOP')
try:
   while True:
      pyautogui.moveRel(30, duration=0.50)
      pyautogui.moveRel(-30, duration=0.50)
      time.sleep(3)
      
      
except KeyboardInterrupt:
   print('GET BACK TO WORK')
