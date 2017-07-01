# Program for "Stopwatch: The Game"
# author: ShenHengheng
import simplegui

# define global variables
n = 0 
tick = 0
success = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(n):
    """format string A:BC.D"""
    if n / 600 >= 10:
        return "Out time"
    elif (n /10) % 60 < 10:
        return str(n / 600) + ":" + "0" + str((n /10) % 60) + "." + str(n % 10)
    else:     
        return str(n / 600) + ":" + str((n /10) % 60) + "." + str(n % 10)

def result(success, tick):
    """rerurn as success/tick formt string """
    return str(success) + '/' + str(tick)

# define event handlers for /buttons; "Start", "Stop", "Reset"
def start():
    """handler function 1 for button start"""
    t.start()

def stop():
    """handler function 2 for button stop"""
    global tick,success
    tick += 1
    t.stop()
  
    if n % 10 == 0:
        success += 1

def reset():
    """Reset time to 0:00.0 """
    global n, tick, success
    tick = 0
    success = 0
    n = 0
    t.stop()

# define event handler for timer with 0.1 sec interval
def time_handler():
    """define event handler for timer with 0.1 sec interval"""
    global n
    n += 1
    

# define draw handler
def draw(canvas):
    """draw handler for canvas"""
    canvas.draw_text(format(n),[70,100],34,"white","serif")
    canvas.draw_text(result(success, tick),[210,20],23,"green")
     
# create frame
f = simplegui.create_frame("StopWatchGame", 250, 200)
t = simplegui.create_timer(100,time_handler)

# register event handlers
f.add_label("Start:",100)
f.add_button("Start",start,100)
f.add_label("Stop:",100)
f.add_button("Stop",stop,100)
f.add_label("Reset",100)
f.add_button("Reset",reset,100)
f.set_draw_handler(draw)

# start frame
f.start()
