import RPi.GPIO as GPIO
import time


p1 = 13
p2 = 15
p3 = 16
p4 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(p1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def gray2binary(gray):
    binary = gray
    while gray > 0:
        gray >>= 1
        binary ^= gray
        
    return binary

position = 0

while True:
    p1State = 1 - GPIO.input(p1)
    p2State = 1 - GPIO.input(p2)
    p3State = 1 - GPIO.input(p3)
    p4State = 1 - GPIO.input(p4)
    
    gray = int(str(p4State) + str(p3State) + str(p2State) + str(p1State), 2)
       
    # convert gray code to binary
    binary = gray2binary(gray)
    
#    position  = int(binary, 2)
    print(p1State, p2State, p3State, p4State, binary)
    
    time.sleep(1)