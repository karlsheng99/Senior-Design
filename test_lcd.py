import RPi.GPIO as GPIO
import RGB1602
import time
import math


def display(lcd, task_name, color, time):
	lcd.setCursor(0, 0)
	lcd.printout(task_name)
	lcd.setCursor(0, 1)
	lcd.printout(str(round(time, 1)))
	lcd.setRGB(color[0], color[1], color[2])

buttonState = True
timerState = False
task_name = 'task1'
color = (148, 0, 110)
lcd = RGB1602.RGB1602(16, 2)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#display(lcd, task_name, color)
start_time = time.time()
current_time = time.time()

while True:
	buttonState = GPIO.input(18)
	if timerState == True:
		current_time = time.time()
	display(lcd, task_name, color, start_time - current_time)

	if buttonState == False and timerState == False:
 		timeState = True
		start = time.time()
	elif buttonState == False and timerState == True:
		timeState = False

