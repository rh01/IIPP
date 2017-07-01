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

 

# initialize ball_pos and ball_vel for new bal in middle of table direction
# if direction is RIGHT, the ball's velocity is upper right, else upper left 
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [ 60 / 60,  - 60 / 60]
    if direction == RIGHT:
        ball_vel[0] = - ball_vel[0]

        
        



# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(RIGHT)


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    # Update ball position
    ball_pos[0] += ball_vel[0]
    print "Current Position", ball_pos[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    if ball_pos[0] <= BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
        print ""
        print "Note:"
        print "Though it says that the position of the ball on the x axis is 19.33..," 
        print "remember that the position is meassured only from the midpoint of the ball."
        print "What we care about is the outer edge of the ball. Why? Because that is the point"
        print "where the ball bounces off the wall and moves into the opposite direction"
        print "(i.e. from left to right). Since the radius of the ball is 20, we find the"
        print "position of the outer edge of the ball by doing 'midpoint - radius'. In this"
        print "case being '(midpoint) 19.33 - 20 (radius)'. The result is less than 0 and"
        print "we have reached the point where we want the ball to bounce off. From now on,"
        print "we will no longer subract 0.66, but add 0.66 to the value on the x axis"
        print ""
        print "Point after Collision", ball_vel
        print ""
    elif WIDTH - ball_pos[0] < BALL_RADIUS:
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[1] < BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif HEIGHT - ball_pos[1] < BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
        
        
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",new_game,100)


# start frame
new_game()
frame.start()
