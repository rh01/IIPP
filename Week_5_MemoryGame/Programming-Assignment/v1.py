# implementation of card game - Memory

import simplegui
import random

NUM_LIST = range(8)*2
DECK_WIDTH = 800
DECK_HEIGHT = 100
CARD_WIDTH = 50
CARD_HEIGHT = 100
NUM_HEIGHT = DECK_HEIGHT * 2 / 3
turn = 0



# helper function to initialize globals
def new_game():
    global NUM_LIST
    
    random.shuffle(NUM_LIST)
    print NUM_LIST

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        canvas.draw_text(str(NUM_LIST[i]), [i * CARD_WIDTH, NUM_HEIGHT], 60, "White" )
     
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric