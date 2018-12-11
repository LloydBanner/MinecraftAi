import time
from input_handling import input_handler

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
    
setup()
