import time
import ctypes
from keyboard_inputs import PressKey, ReleaseKey


W = 0x11
A = 0x1E
S = 0x1F
D = 0x20

MOUSE_LEFTDOWN = 0x0002     # left button down 
MOUSE_LEFTUP = 0x0004       # left button up 
MOUSE_RIGHTDOWN = 0x0008    # right button down 
MOUSE_RIGHTUP = 0x0010      # right button up 
MOUSE_MIDDLEDOWN = 0x0020   # middle button down 
MOUSE_MIDDLEUP = 0x0040     # middle button up
MOUSE_MOVE = 0x0001

def setup():
    time.sleep(3)
    #move_mouse(100, 0)
    #mouse_press_left()
    key_press(A)
    time.sleep(10)
    #mouse_release_left()
    key_release(A)

def move_mouse(x, y):
    ctypes.windll.user32.mouse_event(MOUSE_MOVE, x, -y, 0, 0)

def mouse_press_left():
    ctypes.windll.user32.mouse_event(MOUSE_LEFTDOWN, 0, 0, 0, 0)

def mouse_release_left():
    ctypes.windll.user32.mouse_event(MOUSE_LEFTUP, 0, 0, 0, 0)

def mouse_press_right():
    ctypes.windll.user32.mouse_event(MOUSE_RIGHTDOWN, 0, 0, 0, 0)

def mouse_release_right():
    ctypes.windll.user32.mouse_event(MOUSE_RIGHTUP, 0, 0, 0, 0)

SendInput = ctypes.windll.user32.SendInput

def key_press(key):
    PressKey(key)
    
def key_release(key):
    ReleaseKey(key)  

setup()

