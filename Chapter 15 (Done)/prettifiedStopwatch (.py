#! python3
# stopwatch.py - A simple stopwatch program.


import time, pyperclip


# Display the program's instructions.
print('Press Enter to begin. Afterwards, press ENTER to "click" the stopwatch. Press CTRL-C to quit.')
input()                  # press Enter to begin
print('Started.')
startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1


try:
   while True:
      input()
      lapTime = round(time.time() - lastTime, 2) 
      totalTime = round(time.time() - startTime, 2) 
      string = 'Lap #%s: %s (%s)' % (lapNum, str(totalTime).rjust(6), str(lapTime).rjust(7))
      print(string)
      pyperclip.copy(string)
      lapNum += 1
      lastTime = time.time()     # reset the last lap time
except KeyboardInterrupt:
   # Handle the CTRL-C exception to keep its error message from displaying.
   print('\nDone.')
      
 
