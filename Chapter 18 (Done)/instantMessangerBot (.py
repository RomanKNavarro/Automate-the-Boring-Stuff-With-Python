#! python3
# sends an email to a group of people

import pyautogui, time


compose = (35, 174)
composeColor = (234,  67,  53)


friends = ['armando.romero@aspirestudent.org', 'vicente.guzman@aspirestudent.org', 'roman.navarro@gmail.org', 'manava0470@gmail.com']
subject = 'test100543'
body = 'THIS IS A TEST. CARRY ON.'


while not pyautogui.pixelMatchesColor(compose[0], compose[1], composeColor):
   print('COMPOSE NOT FOUND')
   time.sleep(3)

pyautogui.PAUSE = 2   
pyautogui.click(compose[0], compose[1])


for friend in friends:
   pyautogui.typewrite(friend)
   pyautogui.press('enter')


pyautogui.typewrite('\t' + subject + '\t' + body)
pyautogui.hotkey('ctrl', 'enter')

