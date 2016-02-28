import simplegui
import random

NUMBERS_LIST = range(0,8)*2
NUM_NUMBERS = len(NUMBERS_LIST)
DECK_WIDTH = 800
DECK_HEIGHT = 100
CARD_WIDTH = DECK_WIDTH / NUM_NUMBERS

# helper function to initialize globals
def new_game():
    global shuffle_list, turns, exposed_list, selected, state
    shuffle_list = list(NUMBERS_LIST)
    random.shuffle(shuffle_list)
    turns = 0
    exposed_list = [ False for n in NUMBERS_LIST ]
    label.set_text("Turns = 0")
    selected = []
    state = 0
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed_list, selected, state, turns
    index = pos[0] // CARD_WIDTH
    if not exposed_list[index]:
        if state == 0:
            state = 1
        elif state == 1:
            turns += 1
            label.set_text("Turns = "+str(turns))
            state = 2
        else: # state == 2 from state 1
            if shuffle_list[selected[0]] !=  shuffle_list[selected[1]]:
                exposed_list[selected[0]] = exposed_list[selected[1]] = False
            selected = []     
            state = 1
        selected.append(index)     
        exposed_list[index] = True        
    #print selected, state, turns
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(0, NUM_NUMBERS):
        if exposed_list[i]:
            canvas.draw_text(str(shuffle_list[i]), (i*CARD_WIDTH+10 , DECK_HEIGHT/2 + 13), 50, "White")
        else:
            canvas.draw_polygon([(i*CARD_WIDTH, 0),
                                  ((i+1)*CARD_WIDTH, 0),
                                  ((i+1)*CARD_WIDTH, DECK_HEIGHT),
                                  (i*CARD_WIDTH, DECK_HEIGHT)],
                                  1, "Red", "Green")
    if all(exposed_list):
        canvas.draw_text("You win!!!", (DECK_WIDTH/2-70, DECK_HEIGHT), 30, "Red")  

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", DECK_WIDTH, DECK_HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()