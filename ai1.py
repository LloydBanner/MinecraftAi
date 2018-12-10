import time
import ctypes
from pynput.mouse import Controller
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

icon_x = 619
icon_y = 800
#Minecraft resume button location on bedrock, fullscreen 1080p
resume_x = 574
resume_y = 420

#opens minecraft window and unpauses game if minecraft icon is fourth on hotbar
def setup():
    set_mouse(icon_x, icon_y)
    mouse_press_left()
    mouse_release_left()
    time.sleep(0.05)
    set_mouse(resume_x, resume_y)
    mouse_press_left()
    mouse_release_left()

def set_mouse(x, y):
    width, height = get_mouse_position()
    y_move = y - height
    x_move = x - width
    move_mouse(x_move, y_move)

def move_mouse(x, y):
    x = (x / 3.66)
    y = (y / 3.11)
    ctypes.windll.user32.mouse_event(MOUSE_MOVE, int(x), int(y), 0, 0)

def get_mouse_position():
    mouse = Controller()
    return mouse.position

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

