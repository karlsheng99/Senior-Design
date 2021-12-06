import RPi.GPIO as GPIO
import RGB1602
import time
import math


def display(lcd, row1, row2, color):
    lcd.clear()
    cursor1 = int((16 - len(row1)) / 2)
    cursor2 = int((16 - len(row2)) / 2)
    lcd.setCursor(cursor1, 0)
    lcd.printout(row1)
    lcd.setCursor(cursor2, 1)
    lcd.printout(row2)
    lcd.setRGB(color[0], color[1], color[2])
    
    
def print_time(time):
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)
    s = round(s, 1)
    
    ss = str(s)
    mm = str(int(m))
    hh = str(int(h))
    
    if s < 10:
        ss = '0' + ss
    if m < 10:
        mm = '0' + mm
    if h < 10:
        hh = '0' + hh
        
    return hh + ':' + mm + ':' + ss

buttonState = True
timerState = False
task_name = 'task1'
color = (148, 0, 110)
lcd = RGB1602.RGB1602(16, 2)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

start_time = time.time()
current_time = time.time()
pause_time = time.time()
pause = False

display(lcd, task_name, 'Press the button',color)

while True:
    buttonState = GPIO.input(11)

    if buttonState == False and timerState == False:
        timerState = True
        if pause == True:
            start_time += time.time() - pause_time
        else:
            start_time = time.time()
    elif buttonState == False and timerState == True:
        timerState = False
        pause = True
        pause_time = time.time()

    if timerState == True:
        current_time = time.time()
        timer = print_time(current_time - start_time)
        display(lcd, task_name, timer, color)
    
    time.sleep(0.15)
