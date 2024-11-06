import time 

import pyautogui 

count = 5
print('Rady started go')

for i in range(count):
    print(count)
    time.sleep(1)
    count = -1
    
for i in range(2):
    pyautogui.typewrite('Assalamualikom boro vi ')
    pyautogui.press('enter')
    time.sleep(2)
    