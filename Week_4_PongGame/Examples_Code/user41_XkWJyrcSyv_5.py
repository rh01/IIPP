# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
Vel = 0


# initialize ball_pos and ball_vel for new bal in middle of table direction
# if direction is RIGHT, the ball's velocity is upper right, else upper left 
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [ random.randrange(120, 240)/60,
                 random.randrange(60, 180)/60]
    if direction == "LEFT":
        ball_vel[0] = - ball_vel[0]
        ball_vel[1] = - ball_vel[1]
        
    elif direction == "RIGHT":
        ball_vel[0] =   ball_vel[0]
        ball_vel[1] = - ball_vel[1]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(random.choice(["LEFT","RIGHT"]))
    paddle1_pos = HEIGHT / 2 
    paddle2_pos = HEIGHT / 2 
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0

    if paddle1_pos >= HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
            
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    # Update ball position
    ball_pos[0] += ball_vel[0]
    print "Current Position", ball_pos[0]
    ball_pos[1] += ball_vel[1]
    
    
    if(ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS - 6):
        if ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = ball_vel[0]+ball_vel[0]*0.1
        else:
            score1 = score1 + 1
            spawn_ball("LEFT")
    elif(ball_pos[0] <= PAD_WIDTH + BALL_RADIUS+1):
        if ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:        
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = ball_vel[0]+ball_vel[0]*0.1
        else:
            score2 = score2 + 1
            spawn_ball("RIGHT")
            
    # draw ball
    if ball_pos[0] <= BALL_RADIUS + HALF_PAD_WIDTH:
        ball_vel[0] = - ball_vel[0]
    elif WIDTH - ball_pos[0] < BALL_RADIUS + HALF_PAD_WIDTH:
        ball_vel[0] = -ball_vel[0]
        
    if ball_pos[1] < BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif HEIGHT - ball_pos[1] < BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        

    
        
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    

    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    canvas.draw_polygon([(1, paddle1_pos - HALF_PAD_HEIGHT),
                         (PAD_WIDTH,paddle1_pos - HALF_PAD_HEIGHT),
                         (PAD_WIDTH,paddle1_pos + HALF_PAD_HEIGHT),
                         (1,paddle1_pos + HALF_PAD_HEIGHT)],1,"White","White")
    canvas.draw_polygon([(WIDTH-1, paddle2_pos - HALF_PAD_HEIGHT),
                         (WIDTH-PAD_WIDTH,paddle2_pos - HALF_PAD_HEIGHT),
                         (WIDTH-PAD_WIDTH,paddle2_pos + HALF_PAD_HEIGHT),
                         (WIDTH-1,paddle2_pos + HALF_PAD_HEIGHT)],1,"White","White")

    
    
    
    # determine whether paddle and ball collide paddle1_vel   
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 2 - 50,50), 40, "blue")
    canvas.draw_text(str(score2), (WIDTH / 2 + 30,50), 40, "blue")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle1_vel = 3
    elif key == simplegui.KEY_MAP['up']:
        paddle1_vel = -3
    elif key == simplegui.KEY_MAP['w']:
        paddle2_vel = 3
    elif key == simplegui.KEY_MAP['s']:
        paddle2_vel = -3
        

   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle1_vel = 0
    
    elif key == simplegui.KEY_MAP['up']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['w']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",new_game,100)


# start frame
new_game()
frame.start()
