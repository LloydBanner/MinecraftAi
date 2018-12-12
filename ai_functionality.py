import time
from input_handling import input_handler

turn_90 = 1230 #how far mouse needs to move to turn 90s in x axis
mining_angle = 350 #y axis movement for mining

#opens minecraft window and unpauses game if minecraft icon is fourth on hotbar
#requires player to start facing directly forward
#picaxe item 1 in hotbar and torches item 2
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
    branch_mine(H, 20, 4, 8) #length, spacing, num

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
            blocks = 0
        handler.move_mouse(0, mining_angle)
        handler.mouse_press_left()
        time.sleep(1.1)
        handler.mouse_release_left()
        move_forward(handler, 1)
        handler.move_mouse(0, -mining_angle)

def branch_mine(handler, branch_length, branch_spacing, branch_num):
    branches_mined = 0
    inventory_positions = [(743, 648), (801, 648), (836, 648), (898, 648), (957, 648), (1003, 648), (1056, 648), (1108, 648), (1177, 648),
                           (743, 704), (801, 704), (836, 704), (898, 704), (957, 704), (1003, 704), (1056, 704), (1108, 704), (1177, 704),
                           (743, 760), (801, 760), (836, 760), (898, 760), (957, 760), (1003, 760), (1056, 760), (1108, 760), (1177, 760),
                                                   (836, 820), (898, 820), (957, 820), (1003, 820), (1056, 820), (1108, 820), (1177, 820)]
    for branch in range(branch_num):
        move_forward(handler, (branches_mined * (branch_spacing + 2)))
        mine(handler, branch_spacing + 1)
        right_90(handler)
        mine(handler, branch_length)
        right_90(handler)
        right_90(handler)
        move_forward_jump(handler, branch_length)
        branches_mined += 1
        left_90(handler)
        move_forward(handler, (branches_mined * (branch_spacing + 2)))
        #using chest
        handler.move_mouse(0, mining_angle)
        handler.mouse_press_right()
        time.sleep(0.1)
        handler.mouse_release_right()
        handler.key_press('Lsft')
        for position in inventory_positions:
            handler.set_mouse(position[0], position[1])
            handler.mouse_press_left()
            time.sleep(0.1)
            handler.mouse_release_left()
        handler.key_release('Lsft')
        handler.key_press('E')
        time.sleep(0.1)
        handler.key_release('E')
        handler.move_mouse(0, -mining_angle)
        right_90(handler)
        right_90(handler)
        
    

setup()
