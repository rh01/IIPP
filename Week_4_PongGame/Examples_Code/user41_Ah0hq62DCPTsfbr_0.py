import simplegui
from simplegui import KEY_MAP
import random

#constans
BLOCK_RADIUS = 9
WIDTH = 400
HEIGHT = 400

#starting position and direction of a Snake and Block
start_list_of_blocks = [(WIDTH/2-3*(BLOCK_RADIUS+1), HEIGHT/2-3*(BLOCK_RADIUS+1))]
for i in range(2):
    x = start_list_of_blocks[i]
    start_list_of_blocks.append((x[0] + 2*(BLOCK_RADIUS+1), x[1]))
start_direction = "Right"
while True:
    start_block_position = (random.randrange(10, WIDTH+10, 20), random.randrange(10, HEIGHT+10, 20))
    if start_block_position not in start_list_of_blocks:
        break
score = 0
in_game = None

#Snake class
class Snake:
    def __init__(self, list_of_blocks, start_direction):
        global new_direction, previous_direction, in_game
        
        self.list_of_blocks = list(list_of_blocks)
        new_direction = start_direction
        previous_direction = start_direction 
        in_game = True
        
    def draw(self, canvas):
        for block in self.list_of_blocks:
            canvas.draw_circle(block, BLOCK_RADIUS, 2, "White", "White")
    
    # deletes last Snake's block, add new on the beginning in the proper direction
    # handles colisions with Block object
    # checks whether Snake isn't outside of a game, is so, modyfies variable in_game 
    def update(self):
        global previous_direction, in_game
        
        last = self.list_of_blocks[0]
        first = self.list_of_blocks[len(self.list_of_blocks)-1]
        
        if new_direction == "Right":
            new = (first[0]+2*(BLOCK_RADIUS+1), first[1])
        elif new_direction == "Left":
            new = (first[0]-2*(BLOCK_RADIUS+1), first[1])
        elif new_direction == "Up":
            new = (first[0], first[1]-2*(BLOCK_RADIUS+1))
        elif new_direction == "Down":
            new = (first[0], first[1]+2*(BLOCK_RADIUS+1))
        
        if new in self.list_of_blocks:
            in_game = False
            timer.stop()
        
        if new[0] < 0 or new[0] > WIDTH or new[1] < 0 or new[1] > HEIGHT:
            in_game = False 
            timer.stop()
            
        if new == myBlock.get_coordinates():
            global score
            
            self.list_of_blocks.append(new)
            myBlock.update()
            score += 1
        else:
            self.list_of_blocks.append(new)
            self.list_of_blocks.remove(last)
        
        previous_direction = new_direction
        
    def get_coordinates(self):
        return self.list_of_blocks
    
    def respawn(self, list_of_blocks, start_direction):
        global new_direction, previous_direction, in_game
        
        self.list_of_blocks = list(list_of_blocks)
        new_direction = start_direction
        previous_direction = start_direction 
        in_game = True
        score = 0
        timer.start()
        
#Block class
class Block:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        
    def draw(self, canvas):
        canvas.draw_circle(self.coordinates, BLOCK_RADIUS, 2, "Grey", "Grey")
        
    def update(self):
        while True:
            self.coordinates = (random.randrange(10, WIDTH+10, 20), random.randrange(10, HEIGHT+10, 20))
            if self.coordinates not in mySnake.get_coordinates():
                break
            
    def get_coordinates(self):
        return self.coordinates

#event handlers        
def draw(canvas):
    if in_game == None:
        canvas.draw_text("PySnake", (130,180), 40, "Red")
        canvas.draw_text("Click to start", (160,210), 15, "Red")
    
    if in_game:
        mySnake.draw(canvas)
        myBlock.draw(canvas)
    
    if in_game == False:
        canvas.draw_text('GAME OVER', (WIDTH/4.1, 180), 35, 'Red', 'serif')
        canvas.draw_text("Your score is " + str(score), (WIDTH/3.2, 215), 25, 'Red', 'serif')
        canvas.draw_text('Click to start again', (WIDTH/2.75, 245), 15, 'Red', 'serif')
        
    if score == 361:
        canvas.draw_text('YOU WIN!', (WIDTH/3.5, HEIGHT/2), 35, 'Yellow', 'serif')
        canvas.draw_text("You're amazing!", (WIDTH/3.5, HEIGHT/1.7), 25, 'Yellow', 'serif')
        
def timer_handler():
    mySnake.update()

def key_handler(key):
    global new_direction
    
    if not in_game:
        pass
    elif key == KEY_MAP["right"] and previous_direction != "Left":
        new_direction = "Right"
        mySnake.update()
    elif key == KEY_MAP["left"] and previous_direction != "Right":
        new_direction = "Left"
        mySnake.update()
    elif key == KEY_MAP["up"] and previous_direction != "Down":
        new_direction = "Up"
        mySnake.update()
    elif key == KEY_MAP["down"] and previous_direction != "Up":
        new_direction = "Down"
        mySnake.update()

def mouse_handler(position):
    global score
    
    if in_game == None:
        global mySnake, myBlock
        
        mySnake = Snake(start_list_of_blocks, start_direction)
        myBlock = Block(start_block_position)
        timer.start()
    
    if not in_game:
        myBlock.update()
        mySnake.respawn(start_list_of_blocks, start_direction)
        score = 0
    
        

frame = simplegui.create_frame("PySnake", WIDTH, HEIGHT)
timer = simplegui.create_timer(300, timer_handler)


#register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_handler)
frame.set_mouseclick_handler(mouse_handler)
label1 = frame.add_label('Use the arrow keys to control the snake.')

#let's rock!
frame.start()
 
                