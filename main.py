import RPi.GPIO as GPIO
import encoder
import RGB1602
import lcd
import time
from playground import readfile, writefile

# encoder pins
p1 = 13
p2 = 15
p3 = 16
p4 = 18

# push button pin
b1 = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(p1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(p4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(b1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

colors = [(80, 91, 199),
          (188, 66, 39),
          (228, 159, 51),
          (84, 153, 42),
          (132, 0, 150),
          (92, 148, 195),
          (191, 71, 120),
          (124, 174, 40)]

lcd1602 = RGB1602.RGB1602(16, 2)

# tasks, hours = readfile.readfile('playground/files/test.csv')

while True:
    tasks, hours = readfile.readfile('playground/files/test.csv')

    # rotary encoder position
    p1State = 1 - GPIO.input(p1)
    p2State = 1 - GPIO.input(p2)
    p3State = 1 - GPIO.input(p3)
    p4State = 1 - GPIO.input(p4)
    
    binary, position = encoder.readPosition(p1State, p2State, p3State, p4State)
    
    # task_name = 'task' + str(position) + ' ' + str(binary)
    task_name = tasks[position]

    color = colors[position]

    lcd.display(lcd1602, task_name, 'Press the button',color)
    
    buttonState = GPIO.input(b1)
    if buttonState == False:
        new_position = position
        
        buttonState = True
        timerState = False
        start_time = time.time()
        current_time = time.time()
        pause_time = time.time()
        pause = False
        
        while new_position == position:
            # rotary encoder position
            p1State = 1 - GPIO.input(p1)
            p2State = 1 - GPIO.input(p2)
            p3State = 1 - GPIO.input(p3)
            p4State = 1 - GPIO.input(p4)
            
            new_binary, new_position = encoder.readPosition(p1State, p2State, p3State, p4State)
            
            buttonState = GPIO.input(b1)

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
                timer = lcd.print_time(current_time - start_time)
                lcd.display(lcd1602, task_name, timer, color)
            
            time.sleep(0.15)
        hour = current_time - start_time
        writefile.update_hour('playground/files/test.csv', position, hour)
    time.sleep(0.15)

