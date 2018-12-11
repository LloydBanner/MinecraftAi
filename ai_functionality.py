import time
from input_handling import input_handler

turn_90 = 1230

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
    #move_forward(10, H)
    right_90(H)
    time.sleep(1)
    left_90(H)

def move_forward(n_blocks, handler):
    t = n_blocks * 0.23 #about 0.23s per block
    handler.key_press('W')
    time.sleep(t)
    handler.key_release('W')

def right_90(handler):
    handler.move_mouse(turn_90, 0)

def left_90(handler):
    handler.move_mouse(-turn_90, 0)

setup()
