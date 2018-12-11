import time
from input_handling import input_handler

turn_90 = 1230 #how far mouse needs to move to turn 90s in x axis
mining_angle = 350 #y axis movement for mining

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
    time.sleep(0.07)
    branch_mine(H, 10, 3, 30) #length, spacing, num

def move_forward(handler, n_blocks):
    t = n_blocks * 0.25 #about 0.25s per block
    handler.key_press('W')
    time.sleep(t)
    handler.key_release('W')

def move_forward_jump(handler, n_blocks):
    handler.key_press('W')
    for jump in range(n_blocks):
        handler.key_press('spc')
        time.sleep(0.1)
        handler.key_release('spc')
        time.sleep(0.2)
    handler.key_release('W')

def right_90(handler):
    handler.move_mouse(turn_90, 0)

def left_90(handler):
    handler.move_mouse(-turn_90, 0)

def mine(handler, length):
    #diamond pickaxe in slot 1
    handler.key_press('1')
    time.sleep(0.05)
    handler.key_release('1')
    blocks = 0
    #torch placement
    for block in range(length):
        blocks += 1
        if blocks == 5:
            left_90(handler)
            handler.key_press('2')
            time.sleep(0.05)
            handler.key_release('2')
            handler.mouse_press_right()
            time.sleep(0.1)
            handler.mouse_release_right()
            right_90(handler)
            handler.key_press('1')
            time.sleep(0.05)
            handler.key_release('1')
            
        handler.move_mouse(0, mining_angle)
        handler.mouse_press_left()
        time.sleep(1)
        handler.mouse_release_left()
        move_forward(handler, length)
        handler.move_mouse(0, -mining_angle)

def branch_mine(handler, branch_length, branch_spacing, branch_num):
    branches_mined = 0
    for branch in range(branch_num):
        mine(handler, branch_spacing + 1)
        right_90(handler)
        mine(handler, branch_length)
        right_90(handler)
        right_90(handler)
        move_forward_jump(handler, branch_length)
        right_90(handler)
    

setup()
