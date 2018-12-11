import time
import ctypes
import pyautogui
from keyboard_inputs import PressKey
from keyboard_inputs import ReleaseKey


#opens minecraft window and unpauses game if minecraft icon is fourth on hotbar
def setup():
    H = input_handler()
    icon_x = 768
    icon_y = 1064
    #Minecraft resume button location on bedrock, fullscreen 1080p
    resume_x = 710
    resume_y = 434
    
    H.set_mouse(icon_x, icon_y)
    H.mouse_press_left()
    H.mouse_release_left()
    time.sleep(0.05)
    H.set_mouse(resume_x, resume_y)
    H.mouse_press_left()
    H.mouse_release_left()
    time.sleep(0.05)
    H.key_press('W')
    time.sleep(4)
    H.key_release('W')

class input_handler:

    MOUSE_LEFTDOWN = 0x0002     # left button down 
    MOUSE_LEFTUP = 0x0004       # left button up 
    MOUSE_RIGHTDOWN = 0x0008    # right button down 
    MOUSE_RIGHTUP = 0x0010      # right button up 
    MOUSE_MIDDLEDOWN = 0x0020   # middle button down 
    MOUSE_MIDDLEUP = 0x0040     # middle button up
    MOUSE_MOVE = 0x0001         # mouse movement
        


    def set_mouse(self, x, y):
        width, height = self.get_mouse_position()
        y_move = y - height
        x_move = x - width
        self.move_mouse(x_move, y_move)

    def move_mouse(self, x, y):
        x = (x/3.75)
        y = (y/3.65)
        ctypes.windll.user32.mouse_event(self.MOUSE_MOVE, int(x), int(y), 0, 0)

    def get_mouse_position(self):
        return pyautogui.position()

    def mouse_press_left(self):
        ctypes.windll.user32.mouse_event(self.MOUSE_LEFTDOWN, 0, 0, 0, 0)

    def mouse_release_left(self):
        ctypes.windll.user32.mouse_event(self.MOUSE_LEFTUP, 0, 0, 0, 0)

    def mouse_press_right(self):
        ctypes.windll.user32.mouse_event(self.MOUSE_RIGHTDOWN, 0, 0, 0, 0)

    def mouse_release_right(self):
        ctypes.windll.user32.mouse_event(self.MOUSE_RIGHTUP, 0, 0, 0, 0)

    SendInput = ctypes.windll.user32.SendInput

    def key_press(self, key_string):
        PressKey(key_string)
        
    def key_release(self, key_string):
        ReleaseKey(key_string)  

setup()

