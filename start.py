from operator import truediv
from requests import request
import requests
import RGB1602
import lcd
import subprocess
import time
import RPi.GPIO as GPIO
import os
import signal

lcd1602 = RGB1602.RGB1602(16, 2)

url = 'http://www.google.com'
timeout = 5

while True:
    try:
        request = requests.get(url, timeout=timeout)
        ssid = str(subprocess.check_output(['sudo', 'iwgetid']))
        lcd.display(lcd1602, 'WiFi Connected', ssid.split('"')[1], (144,249,15))
        break
    except(requests.ConnectionError, requests.Timeout) as exception:
        lcd.display(lcd1602, 'No Internet', '', (255,0,0))
        time.sleep(1)

b1 = 37
b2 = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(b1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(b2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

program_state = False
main_pid = 0
server_pid = 0
lt_pid = 0

ip = str(subprocess.check_output(['hostname', '-I']))
ip = ip[2:].split(' ')[0]

while True:
    button_state = GPIO.input(b1)
    signal_state = GPIO.input(b2)

    # run bash script
    if button_state == False and program_state == False:
        lcd.display(lcd1602, 'Loading', ip, (255,209,0))
        
        main = subprocess.Popen(['python', 'home/pi/Senior-Design/main.py'])
        main_pid = main.pid
        server = subprocess.Popen(['python', 'home/pi/Senior-Design/manage.py', 'runserver', '0:8000'])
        server_pid = server.pid
        lt = subprocess.Popen(['lt', '-p', '8000', '-s', 'tasktop'])
        lt_pid = lt.pid

        program_state = True
        time.sleep(0.5)

    # send interrupt signal
    elif button_state == False and program_state == True:
        os.kill(main_pid, signal.SIGTERM)
        os.kill(server_pid, signal.SIGTERM)
        os.kill(lt_pid, signal.SIGTERM)
        lcd.display(lcd1602, 'See You Later', '', (255,209,0))
        program_state = False
        time.sleep(0.5)

    # send shutdown signal
    elif program_state == False and signal_state == False:
        lcd.display(lcd1602, 'Shutting Down', 'Bye Bye', (148,0,110))
        subprocess.call(['sudo', 'shutdown', '-h', '+1'])
        exit()
    
    time.sleep(0.2)