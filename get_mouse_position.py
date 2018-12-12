#not use by program, just to help me out
import pyautogui

running = True
num = 1

while running:
    check = input('continue (y/n): ')
    if check != 'y':
        print('ending program')
        running = False
    else:
        position = pyautogui.position()
        print('position ' + str(num) + ' is: ' + str(position))
        num += 1
