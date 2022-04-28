from os import times
from pathlib import Path
import RPi.GPIO as GPIO
import encoder
import RGB1602
import lcd
import time
from datetime import datetime
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

colors = [(51, 102, 204),
          (16, 150, 24),
          (217, 217, 217),
          (204, 204, 0),
          (255, 153, 0),
          (128, 0, 42),
          (0, 0, 0),
          (184, 46, 138)]

lcd1602 = RGB1602.RGB1602(16, 2)

# tasks, hours = readfile.readfile('playground/files/test.csv')

# If you turn on the device for the first time of the day，
# it will create a folder and files that contain the time data for you.
today = str(datetime.date(datetime.now()))
file_path = '/home/pi/TasktopFiles/' + today + '/'

timestamps_csv_path = '/home/pi/TasktopFiles/timestamps.csv'
stats_path = file_path + 'stats.csv'
timestamps_json_path = file_path + 'timestamps.json'
tasklist_path = file_path + 'tasklist.csv'

if not Path(file_path).exists():
    Path(file_path).mkdir()
    writefile.create_files(stats_path, timestamps_json_path, tasklist_path)


while True:
    color_index, tasks, hours = readfile.readfile(stats_path)

    # rotary encoder position
    p1State = 1 - GPIO.input(p1)
    p2State = 1 - GPIO.input(p2)
    p3State = 1 - GPIO.input(p3)
    p4State = 1 - GPIO.input(p4)
    
    position = encoder.read8Position(p1State, p2State, p3State, p4State)
    
    task_name = tasks[position]

    color = colors[position]

    lcd.display(lcd1602, task_name, 'Press the button',color)
    
    buttonState = GPIO.input(b1)
    if buttonState == False:
        new_position = position
        
        buttonState = True
        timerState = False
        start_time = datetime.now()
        current_time = datetime.now()
        # pause_time = datetime.now()
        # pause = False
        
        while new_position == position:
            # rotary encoder position
            p1State = 1 - GPIO.input(p1)
            p2State = 1 - GPIO.input(p2)
            p3State = 1 - GPIO.input(p3)
            p4State = 1 - GPIO.input(p4)
            
            new_position = encoder.read8Position(p1State, p2State, p3State, p4State)
            
            buttonState = GPIO.input(b1)

            if buttonState == False and timerState == False:
                timerState = True
                # if pause == True:
                #     start_time += datetime.now() - pause_time
                # else:
                #     start_time = datetime.now()
                start_time = datetime.now()
            elif buttonState == False and timerState == True:
                timerState = False
                # pause = True
                # pause_time = datetime.now()
                current_time = datetime.now()
                break

            if timerState == True:
                current_time = datetime.now()
                #timer = lcd.print_time(current_time - start_time)
                timer = current_time - start_time
                timer_sec = lcd.print_time(timer.total_seconds())
                lcd.display(lcd1602, task_name, timer_sec, color)
            
            time.sleep(0.15)
        hour = current_time - start_time
        hour_sec = hour.total_seconds()

        order = writefile.update_task_list(tasklist_path, task_name)

        # add event into files
        writefile.update_timestamps_csv(timestamps_csv_path, position, start_time, current_time)
        writefile.update_timestamps_json(timestamps_json_path, task_name, start_time, current_time)
        writefile.update_stats(stats_path, position, order, hour_sec)
    time.sleep(0.15)

