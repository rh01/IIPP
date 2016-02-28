# implementation of card game - Memory

import simplegui
import random

NUM_LIST = range(8)*2
DECK_WIDTH = 800
DECK_HEIGHT = 100
CARD_WIDTH = 50
CARD_HEIGHT = 100
NUM_HEIGHT = DECK_HEIGHT * 2 / 3
turns = 0



# helper function to initialize globals
def new_game():
    global NUM_LIST, exposed, state, selected, turns
    exposed = [False for i in range(16)]
    random.shuffle(NUM_LIST)
    state = 0
    selected = []
    turns = 0
    label.set_text("Turns = 0")


     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed_list, selected, state, turns
    index = pos[0] // CARD_WIDTH
    if not exposed[index]:
        if state == 0:
            state = 1
        elif state == 1:
            turns += 1
            label.set_text("Turns = "+str(turns))
            state = 2
        else: # state == 2 from state 1
            if NUM_LIST[selected[0]] !=  NUM_LIST[selected[1]]:
                exposed[selected[0]] = exposed[selected[1]] = False
            selected = []     
            state = 1
        selected.append(index)     
        exposed[index] = True 
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        if exposed[i]:
            canvas.draw_text(str(NUM_LIST[i]),
                             [i * CARD_WIDTH + 10, NUM_HEIGHT],
                             60, "White" )
        else:
            canvas.draw_polygon([(i * CARD_WIDTH, 0), 
                                (i * CARD_WIDTH, CARD_HEIGHT), 
                                ((i + 1) * CARD_WIDTH, CARD_HEIGHT), 
                                ((i + 1) * CARD_WIDTH, 0)], 2, 'Red', "Green")
    if sum(exposed) == 16:
        canvas.draw_text("You Win!", [300, 70], 60, "Red")


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