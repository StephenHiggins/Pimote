'''
Created on May 7, 2016

@author: Stephen Higgins
'''

if __name__ == '__main__':
    main() 
    
#!/usr/bin/env python



import socket, OSC, re, time, threading, math, serial, opc 
import RPi.GPIO as GPIO
from time import sleep
import time
import Queue
import random
#comment



# VARIABLES

numLEDs = 24
###### create lists for led iteration #######
ledlist = list(range(24))
#create opposite ledlist
ledlist2 = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
ledlist5 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ledlist3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,0]
ledlist4 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,0,1]

#### led colour lists

ras_col = [(100, 0, 0),(100, 100, 0),(0, 100, 0)]

client = opc.Client('localhost:7890')
receive_address = 'localhost', 7000 # Outgoing Port
send_address = '172.20.10.5', 8000 #DAW Adress, Incoming Port



play_q = Queue.Queue(1)
standby_q = Queue.Queue(1)
rec_q = Queue.Queue(1)
v = 1
black = [ (0,0,0), (0,0,0) ] * numLEDs
tstamp = time.time()

##########################
#
#       Tkinter
#
##########################






##############
#
#Fadecandy LED Functions
#
##############


def play_led():
        
        while not play_q.empty():
                for i,j in zip(ledlist, ledlist2):
                        pixels = [ (0,100,0) ] * numLEDs
                        pixels[i] = (0, 0, 0)
                        pixels[j] = (0, 0, 0)
                        client.put_pixels(pixels)
                        time.sleep(0.03)
                standby_led()
        
def rec_led():
        
        while not rec_q.empty():
                for i,j in reversed(zip(ledlist, ledlist2)):
                        pixels = [ (100,0,0) ] * numLEDs
                        pixels[i] = (0, 0, 0)
                        pixels[j] = (0, 0, 0)
                        client.put_pixels(pixels)
                        time.sleep(0.01)
                standby_led()
"""


or i,j in reversed(zip(ledlist, ledlist2)):
                        pixels = [ (100,0,0) ] * numLEDs
                        pixels[i] = (0, 0, 0)
                        pixels[j] = (0, 0, 0)
                        client.put_pixels(pixels)
                        time.sleep(0.01)

def revscrub_led():
        
        while not revscrub_q.empty():
                for i,j in reversed(zip(ledlist, ledlist2)):
                        pixels = [ (100,0,0) ] * numLEDs
                        pixels[i] = (0, 0, 0)
                        pixels[j] = (0, 0, 0)
                        client.put_pixels(pixels)
                        time.sleep(0.01)
                standby_led()

def pause_led():
        
        while not pause_q.empty():
                for i,j in zip(range(0,24,1), (range(23,-1,-1))):
                        pixels = [ (0,100,0) ] * numLEDs
                        pixels[i] = (0, 0, 0)
                        pixels[j] = (0, 0, 0)
                        client.put_pixels(pixels)
                        time.sleep(0.03)
                standby_led()
"""
def standby_led():
        while not standby_q.empty():
                #random.shuffle(ledlist)
                random.shuffle(ledlist3)
                random.shuffle(ledlist4)
                for i,j,k in zip(ledlist, ledlist3, ledlist4):
                        pixels = [ (0,0,0) ] * numLEDs
                        pixels[i] = (100, 0, 0)
                        pixels[j] = (100, 100, 0)
                        pixels[k] = (0, 100, 0)
                        client.put_pixels(pixels)
                        time.sleep(0.01)

        if not play_q.empty():
                play_led()
        elif not rec_q.empty():
                rec_led()                
        else:
                return

"""
def standby_led():
        while not standby_q.empty()and not dead:
               for i in range(24):
                   red = [100, 0, 0] * 8
                   yellow = [100, 100,0] * 8
                   green = [0, 100, 0] * 8
                   client.put_pixels(red)
                   client.put_pixels(yellow)
                   client.put_pixels(green)
                              
                        
        

"""

############
#GPIO Setup
############

GPIO.setmode(GPIO.BCM)

Bplay = 6
Bstop = 13
Brec = 5

GPIO.setup(Bplay, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(Bstop, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(Brec, GPIO.IN, pull_up_down = GPIO.PUD_UP)

class PiException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#########################
#
#
#Button detection
#
#
#
#########################

# interrupt callbacks for button detection
def button_callback():
    GPIO.add_event_detect(Bplay, GPIO.FALLING, callback=play)
    GPIO.add_event_detect(Bstop, GPIO.FALLING, callback=stop)
    GPIO.add_event_detect(Brec, GPIO.FALLING, callback=record)



##########################
#    OSC
##########################

# Initialize the OSC server and the client.
s = OSC.OSCServer(receive_address)
c = OSC.OSCClient()
c.connect(send_address)

#s.addDefaultHandlers()

# define a message-handler function for the server to call.
def test_handler(addr, tags, stuff, source):
    print "---"
    print "received new osc msg from %s" % OSC.getUrlStr(source)
    print "with addr : %s" % addr
    print "typetags %s" % tags
    print "data %s" % stuff
    msg = OSC.OSCMessage()
    msg.setAddress(addr)
    msg.append(stuff)
    c.send(msg)
    print "return message %s" % msg
    print "---"

def stop_mh(add, tags, stuff, source):
        print "stop"
        standby_led()

def play_mh(add, tags, stuff, source):
    print "play"
    play_led()

#########################
#
# Outgoing OSC Message Functions
#
########################

def play(channel):
        global tstamp
        time_now = time.time()
        if (time_now - tstamp) >= 0.3:
                if not standby_q.empty():
                        print "\nEmptying Standby queue"
                        i = standby_q.get()
                elif not rec_q.empty():
                        print "\nEmptying Record queue"
                        i = rec_q.get()

                if play_q.empty():
                        print "\nFilling Play queue"
                        play_q.put(v)
                else:
                        print "play queue already full!"
                        
                print("Play")
                msg = OSC.OSCMessage()
                msg.setAddress("/play")
                c.send(msg)
        tstamp = time_now
        
def record(channel):
        global tstamp
        time_now = time.time()
        if (time_now - tstamp) >= 0.3:
                if not standby_q.empty():
                        print "\nEmptying Standby queue"
                        i = standby_q.get()
                elif not play_q.empty():
                        print "\nEmptying Play queue"
                        i = play_q.get()

                if rec_q.empty():
                        print "\nPutting to Record Queue"
                        rec_q.put(v)
                else:
                        print "\nRecord queue already full!"

                print("Record")
                msg = OSC.OSCMessage()
                msg.setAddress("/record")
                c.send(msg)
        tstamp = time_now

def stop(channel):
        global tstamp
        time_now = time.time()
        if (time_now - tstamp) >= 0.1:
                if not play_q.empty():
                        print "\nEmptying Play queue"
                        i = play_q.get()
                elif not rec_q.empty():
                        print "\nEmptying Record queue"
                        i = rec_q.get()

                if standby_q.empty():
                        print "\nFilling Standby Queue"
                        standby_q.put(v)
                else:
                        print "Standby queue already full!"
                
                print("Stop")
                msg1 = OSC.OSCMessage()
                msg1.setAddress("/stop")
                c.send(msg1)
        tstamp = time_now



# adding incoming message handler pointers

s.addMsgHandler("/stop", stop_mh)
#s.addMsgHandler("/pause", moveJoystick_handler)
s.addMsgHandler("/play", play_mh)

# just checking which handlers we have added
print "Registered Callback-functions are :"
for addr in s.getOSCAddressSpace():
    print addr

# kick off the standy_led function by adding a value to standy_q
print "\nStarting LED Queue"
standby_q.put(v)
# Start OSCServer
print "\nStarting OSCServer. Use ctrl-C to quit."

st = threading.Thread( target = s.serve_forever )
st.daemon = True
st.start()
st.name = "OSC Server Thread"
print "\nStarting LED thread"
led_thread = threading.Thread ( target = standby_led )
led_thread.daemon = True
led_thread.start()
led_thread.name = "LED Thread"
print "\nStarting button detection thread"
btn_thread = threading.Thread ( target = button_callback )
btn_thread.daemon = True
btn_thread.start()
btn_thread.name = "Button Thread"
print"\n************************"
print (threading.enumerate())
print"\n************************"
       
# Loop while threads are running.
try :
    while True:
                             
               gui.main()

except KeyboardInterrupt :
    print "\nClosing OSCServer..."
    s.close()
    print "Done"
    print "\nClosing LED Threads..."
    client.put_pixels(black)
    
    print "Done"
    print "Waiting for Server and Detection threads to finish"
    st.join()
    print "Done"
    GPIO.cleanup()
finally:
        print "\nClosing OSCServer..."
    s.close()
    print "Done"
    print "\nClosing LED Threads..."
    client.put_pixels(black)
    
    print "Done"
    print "Waiting for Server and Detection threads to finish"
    st.join()
    print "Done"
    #GPIO.cleanup()
    