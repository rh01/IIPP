# Implementation of almoust classic arcade game Pong
############## created by Viacheslav Pronin. Kremenchug, Ukraine ##############

import simplegui
import random
import math

# initialize globals 
width = 600
height = 400       
ball_radius = 10
pad_width = 8

half_pad_width = pad_width / 2
left = False
right = True
bonus_status = "ON"
ball_color = 'white'
pad_color1 = 'white'
pad_color2 = 'white'
score1 = 0
score2 = 0
bonus_value = ' '
bonus_color = 'black'
bonus_speed = 0
bonus_pos = [0,0]
rockets1 = 0
rockets2 = 0
rocket_pos = [width*2, height * 2]
rocket_speed = 0
max_ball_speed = 0

### STARS' COORDINATES FOR MENU ###
stars_amount = 500
star = [[0,0]]*stars_amount
for i in range(stars_amount):
    star[i] = random.randint(pad_width, width-pad_width), random.randint(0, height)
    
    
def bonus_timer():
    global bonus_value, bonus_color, bonus_speed, bonus_pos, game_mode    
    bonus_value = random.choice (['-','+','L','S','R','R','R'])  # more rockets for more fun
    if bonus_value == '-' or bonus_value == 'S':
        bonus_color = 'red'
    else: 
        bonus_color = 'lime'
    bonus_speed = 3 * random.randrange(-1,game_mode,2)  # multiplier is the direction 
    bonus_pos = [width/2, random.randrange(20, height-20)]
    
def catch(player):			
    global bonus_pos, bonus_value, pad_height1, pad_height2, rockets1, rockets2, score1, score2
    global pad_color1, pad_color2
    bonus_pos = [width/2, height * 2]  #remove bonus from screen
    if player == 1:
        if bonus_value == '-':
            score1 -= 1
        if bonus_value == '+':
            score1 += 1
        if bonus_value == 'L':
            pad_height1 *= 1.5
        if bonus_value == 'S':
            pad_height1 *= 0.75  
        if bonus_value == 'R':
            rockets1 += 1     
        if bonus_value == '-' or bonus_value == 'S':
            pad_color1 = 'red'
        else: pad_color1 = 'lime'

    if player == 2:
        if bonus_value == '-':
            score2 -= 1
        if bonus_value == '+':
            score2 += 1
        if bonus_value == 'L':
            pad_height2 *= 1.5
        if bonus_value == 'S':
            pad_height2 *= 0.75 
        if bonus_value == 'R':
            rockets2 += 1  
        if bonus_value == '-' or bonus_value == 'S':
            pad_color2 = 'red'
        else: pad_color2 = 'lime'
    timer2.start()
    
### Rocket launcher
def launch(player):
    global rockets1, rockets2, rocket_pos, rocket_speed, paddle1_pos, paddle2_pos
    global pad_heght1, pad_height2
    if rocket_pos[0] > width or rocket_pos[0] < 0:    #only 1 rocket can be present on the screen
        if player == 1:
            rocket_pos[0] = pad_width
            rocket_pos[1] = paddle1_pos + pad_height1/2
            rocket_speed = 15
            rockets1 -= 1
        if player == 2:
            rocket_pos[0] = width - pad_width 
            rocket_pos[1] = paddle2_pos + pad_height2/2
            rocket_speed = -15
            rockets2 -= 1
            
# If you catch something, your pad will be coloured for some time
def color_timer():
    global pad_color1, pad_color2
    pad_color1 = 'white'
    pad_color2 = 'white'
    timer2.stop()

# Stop and color the ball if round is over 
def ball_timer():
    global ball_color, direction
    ball_color = 'white'
    timer3.stop()
    spawn_ball(direction)
    
### SPAWN BALL, START VELOCITY ####
def spawn_ball(direction):
    global ball_pos, ball_vel, acceleration, pad_height1, pad_height2, rocket_pos # these are vectors stored as lists
    ball_pos = [width/2, height/2]
    pad_height1 = 80
    pad_height2 = 80
    rocket_pos = [width*2, height * 2] #remove previous rocket from screen
    acceleration = 1
    if direction:
        vel_sign = 1		#right
    else: vel_sign = -1		#left
    ball_vel = [vel_sign * random.randrange(2,5),-random.randrange(1, 3)]
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global game_mode, mode_selector, bonus_pos, rockets1, rockets2
    global pad_height1, pad_height2, max_ball_speed
    timer.stop()
    game_mode = 0		# 0: menu; 1: 1 player, 2: 2 players
    mode_selector = 1	# position of menu cursor
    bonus_pos = [width/2, height * 2]  #remove previous bonus from screen
    score1 =0
    score2 = 0
    rockets1 = 0
    rockets2 = 0
    paddle1_vel = 0
    paddle2_vel = 0
    pad_height1 = 80
    pad_height2 = 80
    paddle1_pos = height / 2 - pad_height1 / 2
    paddle2_pos = height / 2 - pad_height2 / 2
    max_ball_speed = 0
    
    if score1 > score2:
        direction = True	# True = right, False = left
    elif score1 < score2:
        direction = False
    else: direction = bool(random.randrange(0,2))
    spawn_ball(direction)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, ball_color
    global pad_height1, pad_height2, acceleration, paddle2_vel
    global mode_selector, game_mode, direction
    global bonus_value, bonus_pos, bonus_color, bonus_speed 
    global rocket_pos, rocket_speed, rockets1, rockets2
    global pad_color1, pad_color2, max_ball_speed
    
  
    # draw mid line and gutters
    canvas.draw_line([width / 2, 0],[width / 2, height], 1, "White")
    canvas.draw_line([pad_width, 0],[pad_width, height], 1, "White")
    canvas.draw_line([width - pad_width, 0],[width - pad_width, height], 1, "White")
    
    ### START MENU ###   
    if game_mode == 0:
        for i in range(stars_amount): 
            canvas.draw_point(star[i], 'grey')  #stars
        canvas.draw_text('Choose mode:', (20 , height /2), 30, 'White', "monospace") 
        canvas.draw_text('1 player', (40 , height /2+30), 30, 'White', "monospace")    
        canvas.draw_text('2 players', (40 , height /2+60), 30, 'White', "monospace")
        canvas.draw_text('Bonuses are ' + bonus_status, (40 , height /2+90), 30, 'White', "monospace")
        canvas.draw_text('>', (20 , height /2 + mode_selector * 30), 30, 'lime','monospace') 
        canvas.draw_text('to navigate use space',(40 , height /2+120), 20, 'grey', "monospace")
        canvas.draw_text('and up/down buttons',(40 , height /2+140), 20, 'grey', "monospace")
        
        canvas.draw_text('Controls:', (width/2 + 5 , 50), 25, 'grey', "monospace")
        canvas.draw_text('W/S     - paddle 1 up/down', (width/2 + 5 , 80), 20, 'grey', "monospace")
        canvas.draw_text('Up/Down - paddle 2 up/down', (width/2 + 5 , 100), 20, 'grey', "monospace")
        canvas.draw_text('Space   - launch rocket #1 ', (width/2 + 5 , 120), 20, 'grey', "monospace")
        canvas.draw_text('Enter   - launch rocket #2 ', (width/2 + 5 , 140), 20, 'grey', "monospace")
        canvas.draw_text('R       - new game', (width/2 + 5 , 160), 20, 'grey', "monospace")
        
        canvas.draw_text('Bonuses:', (width/2 + 5 , 200), 25, 'grey', "monospace")
        canvas.draw_text('S       - shorter pad', (width/2 + 5 , 220), 20, 'grey', "monospace")
        canvas.draw_text('L       - longer pad', (width/2 + 5 , 240), 20, 'grey', "monospace")
        canvas.draw_text('"-"     - minus score', (width/2 + 5 , 260), 20, 'grey', "monospace")
        canvas.draw_text('"+"     - plus score', (width/2 + 5 , 280), 20, 'grey', "monospace")
        canvas.draw_text('R       - rocket', (width/2 + 5 , 300), 20, 'grey', "monospace")
    ### THE GAME ##### 
    else:

    # update ball
        
        if ball_pos[1] >= height - ball_radius or ball_pos[1] <= ball_radius:
            ball_vel[1]= - ball_vel[1]
        if ball_pos[0] >= width - pad_width - ball_radius or ball_pos[0] <= pad_width + ball_radius:
            ball_vel[0]= - ball_vel[0]
        
        ball_pos[0] += ball_vel[0] * acceleration
        ball_pos[1] += ball_vel[1] * acceleration      
        ball_speed = math.hypot(ball_vel[0], ball_vel[1])*acceleration
        if ball_speed > max_ball_speed:
            max_ball_speed = ball_speed
        #print ball_pos                
    # draw ball
        canvas.draw_circle(ball_pos, ball_radius, 2, 'orange', ball_color)   

    ### PADDLE'S POSITION
        if paddle1_pos - paddle1_vel <0: paddle1_pos = 0 
        if paddle1_pos - paddle1_vel > height - pad_height1: paddle1_pos = height - pad_height1    
        if paddle1_pos + paddle1_vel >= 0 and paddle1_pos + paddle1_vel <= height - pad_height1:
            paddle1_pos += paddle1_vel
            
        if game_mode == 1:		### 2nd player is computer
            if  paddle2_pos + pad_height2/8*5 <= ball_pos[1]:
                paddle2_vel = 5
            elif paddle2_pos + pad_height2/8*3 >= ball_pos[1]:
                paddle2_vel = -5
            elif abs(paddle2_pos + pad_height2/2 - ball_pos[1]) <= 2: #hysteresis
                paddle2_vel = 0

        if paddle2_pos - paddle2_vel <0: paddle2_pos = 0 
        if paddle2_pos - paddle2_vel > height - pad_height2: paddle2_pos = height - pad_height2    
        if paddle2_pos + paddle2_vel >= 0 and paddle2_pos + paddle2_vel <= height - pad_height2:
            paddle2_pos += paddle2_vel
    # draw paddles
        canvas.draw_line([half_pad_width, paddle1_pos], [half_pad_width, paddle1_pos+pad_height1], pad_width, pad_color1)
        canvas.draw_line([width-half_pad_width, paddle2_pos], [width-half_pad_width, paddle2_pos+pad_height2], pad_width, pad_color2)
    
    ###   BOUNCES   ###  

        if ball_pos[0] <= pad_width + ball_radius and ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + pad_height1:
            acceleration *= 1.1 
        elif ball_pos[0] <= pad_width + ball_radius and (ball_pos[1] < paddle1_pos or ball_pos[1] > paddle1_pos + pad_height1):            
            score2 += 1
            ball_vel = [0,0]
            ball_pos[0] = pad_width + ball_radius +1
            ball_color = 'red'
            direction = True
            timer3.start()
       
        if ball_pos[0] >= width - pad_width - ball_radius and (ball_pos[1] < paddle2_pos or ball_pos[1] > paddle2_pos + pad_height2):
            score1 += 1
            ball_vel = [0,0]
            ball_pos[0] = width - pad_width - ball_radius - 1
            ball_color = 'red'
            direction = False
            timer3.start()

    ### BONUSES
        if bonus_status == 'ON':
            timer.start()

    ### Draw bonus
            bonus_pos[0] += bonus_speed
            canvas.draw_text(bonus_value, bonus_pos, 30, bonus_color, "monospace")   
    
    ### Draw rocket
            rocket_pos[0] += rocket_speed
            canvas.draw_text('=', rocket_pos, 30, 'Yellow', "monospace")   
            
    ### CATCH THE BONUS
            if bonus_pos[0] > 0 and bonus_pos[0] <= pad_width and bonus_pos[1] >= paddle1_pos and bonus_pos[1]-10 <= paddle1_pos + pad_height1:
                catch(1)
            if bonus_pos[0] < width and bonus_pos[0] >= width - pad_width and bonus_pos[1] >= paddle2_pos and bonus_pos[1]-10 <= paddle2_pos + pad_height2:
                catch(2)      
                
    ### Draw amount of rockets
            canvas.draw_text('I'*rockets1, (50,20), 20, 'yellow', "monospace") # amount of rockets
            canvas.draw_text('I'*rockets2, (width - 50- rockets2*10 ,20), 20, 'yellow', "monospace")
    ### CATCH THE ROCKET :)
            if rocket_speed < 0 and rocket_pos[0] > 0 and rocket_pos[0] <= pad_width and rocket_pos[1] >= paddle1_pos and rocket_pos[1] <= paddle1_pos + pad_height1:
                score1 -= 1
                pad_color1 = 'red'
                timer2.start()
            if rocket_speed > 0 and rocket_pos[0] < width and rocket_pos[0] >= width - pad_width and rocket_pos[1] >= paddle2_pos and rocket_pos[1] <= paddle2_pos + pad_height2:
                score2 -= 1
                pad_color2 = 'red'
                timer2.start()
    # draw scores
        canvas.draw_text(str(score1), (width/4 , 100), 30, 'White', "monospace")
        canvas.draw_text(str(score2), (width/4*3 , 100), 30, 'White', "monospace")
        canvas.draw_text('Ball speed:'+ str(ball_speed)[0:4], (width/5 , height-10), 16, 'grey')
        canvas.draw_text('Max ball speed:'+ str(max_ball_speed)[0:4], (width/5*3 , height-10), 16, 'grey')
def keydown(key):
    global paddle1_vel, paddle2_vel, mode_selector, game_mode, bonus_status, rockets1, rockets2
    #print key
       
    if game_mode == 0:
        if key == 38:								#down key
            if mode_selector >1:
                mode_selector -= 1
        elif key == 40:								#up key
            if mode_selector <3:
                mode_selector += 1
        if mode_selector == 1 and (key == 13 or key == 32):  #space or enter key
            game_mode = 1
        if mode_selector == 2 and (key == 13 or key == 32):
            game_mode = 2
        if mode_selector == 3 and (key == 13 or key == 32):
            if bonus_status == 'ON':
                bonus_status = 'OFF'
            else: bonus_status = 'ON'
    else: 
        if key == 87: paddle1_vel = -5			# W and S keys
        if key == 83: paddle1_vel = 5

        if key == 38: paddle2_vel = -5
        if key == 40: paddle2_vel = 5   
        if rockets1 > 0 and key == 32:			#space and enter key
            launch(1)
        if rockets2 > 0 and key == 13:
            launch(2)
    
    if key == 82: 									#R(reset) key
        new_game()
       
def keyup(key):
    global paddle1_vel, paddle2_vel
    if game_mode != 0:
        if (key == 87 or key == 83): 
            paddle1_vel = 0
        if (key == 38 or key == 40): 
            paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", width, height)
button1 = frame.add_button('New game', new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(random.randrange(5000, 10000), bonus_timer)
timer2 = simplegui.create_timer(300, color_timer)
timer3 = simplegui.create_timer(300, ball_timer)

# start frame
new_game()
frame.start()
