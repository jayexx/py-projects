#International Morse Code generator
#the length of a dot is one unit
#a dash is 3 units
#the space between parts of the same letter is one unit
#the space between letters is 3 units
#the space between words is 7 units
#1 unit = .05 seconds
import time
import os
import sys

#sets message to input and makes it lowercase
message = raw_input("Input message here: ")
message = message.lower()

#assign variables for dot and dash
dot = 'echo -n .'
dash = 'echo -n -'

#assign alternative dots and dashes based on arguement passed to script
if len(sys.argv) > 1:
        if sys.argv[1].lower() == 'ping':
                dot = 'sudo ping -c 1 localhost'
                dash = 'sudo ping -c 1 -s 184 localhost'
        elif sys.argv[1].lower() == 'audio':
                dot = 'aplay dot.wav > /dev/null 2>&1'
                dash = 'aplay dash.wav > /dev/null 2>&1'
        elif sys.argv[1].lower() == 'help':
                print "Program to output messages in Interational Morse Code\nArguments\nPing: Pings purdue.edu in Morse code, 1 unit = 64 bytes including header info\nAudio: outputs audio in morse code using the built in headphone jack, 1 unit == .05 second 540 Hz sine wave\nText: outputs to terminal, 1 unit = .05 seconds\nPlacing tab character at end of message loops it, any other unrecognized character breaks it"

def morse():
        #iterate through message and execute equivalent dot and dash commands for each letter
        for i in message:
                if i == 'a':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                elif i == 'b':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                elif i == 'c':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                elif i == 'd':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                elif i == 'e':
                        os.system(dot)
                elif i == 'f':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                elif i == 'g':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                elif i == 'h':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                elif i == 'i':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                elif i == 'j':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                elif i == 'k':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                elif i == 'l':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                elif i == 'm':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                elif i == 'n':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                elif i == 'o':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                elif i == 'p':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                elif i == 'q':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                elif i == 'r':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                elif i == 's':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                elif i == 't':
                        os.system(dash)
                elif i == 'u':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                elif i == 'v':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                elif i == 'w':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                elif i == 'x':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                elif i == 'y':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                elif i == 'z':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                elif i == '0':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                elif i == '1':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                elif i == '2':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                elif i == '3':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                elif i == '4':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dash)
                elif i == '5':
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                elif i == '6':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                elif i == '7':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                elif i == '8':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                        time.sleep(.05)
                        os.system(dot)
                elif i == '9':
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dash)
                        time.sleep(.05)
                        os.system(dot)
                elif i == ' ':
                        #sleep to make space
                        j = 0
                        while j <= 6:
                                time.sleep(.05)
                                j = j + 1
                elif i == '\t':
                        #return to beginning of message
                        morse()
                else:
                        break
                time.sleep(.15)	

morse()
