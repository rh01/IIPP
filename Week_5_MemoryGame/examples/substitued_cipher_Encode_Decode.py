#cipher encode and decode
import simplegui
import random

CIPHER = {}

LEETERS = 'abcdefghijklmnopqrstuvwxyz'

message = ""

def init():
    letter_list = list(LEETERS)

    random.shuffle(letter_list)
    for ch in LEETERS:
        CIPHER[ch] = letter_list.pop()
    return CIPHER
        
def encode():
    emsg = ""
    for ch in message:
        emsg += CIPHER[ch]
    print 'Encode:' + emsg

def decode():
    dmsg = ""
    for ch in message:
        for key in CIPHER.keys():
            if CIPHER[key] == ch:
                dmsg += key
                
    print 'Decode:' + dmsg


# Update message input
def newmsg(msg):
    global message
    message = msg
    label.set_text(msg)
    
# Create a frame and assign callbacks to event handlers
init()

frame = simplegui.create_frame("Cipher", 2, 200, 200)
frame.add_input("Message:", newmsg, 200)
label = frame.add_label("", 200)
frame.add_button("Encode", encode)
frame.add_button("Decode", decode)
# Start the frame animation
frame.start()