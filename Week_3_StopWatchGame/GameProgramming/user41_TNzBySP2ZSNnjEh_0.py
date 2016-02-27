# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
attempts = 0
successes = 0 
start_game = "0/0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if t < 10:
        format_time = str(t)
        return "0:00." + format_time
    elif t < 100:
        format_time = str(t)
        return "0:0" + format_time[0] + "." + format_time[1]
    elif t <= 599:
        format_time = str(t)
        return "0:" + format_time[0:2] + "." + format_time[2]
    else:
        minutes = t / 600
        #seconds_ten = (t % 600) / 60
        #seconds_one = (t / 10) 
        t2 = (t % 600)
        if t2 < 10:
            format_time = str(t2)
            return str(minutes) + ":00." + format_time
        elif t2 < 100:
            format_time = str(t2)
            return str(minutes) + ":0" + format_time[0] + "." + format_time[1]
        else: 
            format_time = str(t2)
            return str(minutes) + ":" + format_time[0:2]  + "." + format_time[2]
            
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    stop_timer.start()
    
def stop():
    if stop_timer.is_running():
        stop_timer.stop()
        global successes, attempts, start_game
        if time % 10 == 0:
            global successes, attempts, start_game
            successes = successes + 1
            attempts = attempts + 1
            start_game = str(successes) + "/" + str(attempts) 
        else:
            attempts = attempts + 1
            start_game = str(successes) + "/" + str(attempts)
    else:
        pass
    
def reset():
    stop_timer.stop()
    global time, successes, attempts, start_game
    time = 0
    attempts = 0
    successes = 0 
    start_game = "0/0"


# define event handler for timer with 0.1 sec interval
def increm_time():
    global time
    time +=1


# define draw handler
def increm(my_canvas):
    my_canvas.draw_text(format(time), (75, 150), 25, "Red")
    my_canvas.draw_text(start_game, (150, 25), 20, "Green")
    
# create frame
stopwatch = simplegui.create_frame("Stopwatch Game", 200, 300)
stop_timer = simplegui.create_timer(100, increm_time)
stopwatch.add_button("Start", start, 100)
stopwatch.add_button("Stop", stop, 100)
stopwatch.add_button("Reset", reset, 100)



# register event handlers
stopwatch.set_draw_handler(increm)


# start frame
stopwatch.start()

# Please remember to review the grading rubric
