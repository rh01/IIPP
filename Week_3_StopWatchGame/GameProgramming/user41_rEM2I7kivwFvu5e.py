# template for "Stopwatch: The Game"

import simplegui

# define global variables
interval = 100
counter = 0
position = [100, 100]
stopped = 0
try_stop = 0
successful_stop = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(val):
    # minutes
    minutes = int(val / (10*60))
    # hundreths
    hundreth =  val % 10
    #seconds
    if int(val / 10) < 10:
        print_sec = "0" + str(val/10)
    elif int(val / 10) < 60:
        print_sec = str(val / 10)
    elif val / 10 - minutes * 60 < 10:
        print_sec = "0" + str(val / 10 - minutes * 60)
    else:
        print_sec = str(val / 10 - minutes * 60)
    
    stopwatch =  str(minutes) + ":" + print_sec + "." + str(hundreth)
    return stopwatch
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def click_start():
    global counter, stopped
    stopped = 0
    timer.start()
    
# whenever you press stop try_stop increases by 1
# if you press stop at x.xx.0 then successful_stop increases by 1
def click_stop():
    global stopped, counter, try_stop, successful_stop
    timer.stop()
    if stopped == 0:
        try_stop = try_stop + 1
        if counter % 10 == 0:
            successful_stop = successful_stop + 1
    stopped = 1
    
def click_reset():
    global counter, try_stop, successful_stop
    timer.stop()
    counter = 0
    try_stop = 0
    successful_stop = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global counter 
    counter = counter + 1
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter), position, 36, "White")
    canvas.draw_text(str(successful_stop) + "/" + str(try_stop),[240,20],20,"red")
    
# create frame
frame = simplegui.create_frame("Home", 300, 200)

# register event handlers
frame.add_button("Start", click_start)
frame.add_button("Stop", click_stop)
frame.add_button("Reset", click_reset)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
