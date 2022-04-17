from requests import request
import requests
import RGB1602
import lcd
import subprocess
import time

lcd1602 = RGB1602.RGB1602(16, 2)

url = 'http://www.google.com'
timeout = 5

while True:
    try:
        request = requests.get(url, timeout=timeout)
        ssid = subprocess.check_output(['sudo', 'iwgetid'])
        #lcd.display(lcd1602, 'WiFi Connected', ssid.split('"')[1], (144,249,15))
        lcd.display(lcd1602, 'WiFi Connected', 'TP-Link_057B', (144,249,15))
    except(requests.ConnectionError, requests.Timeout) as exception:
        lcd.display(lcd1602, 'No Internet', '', (255,0,0))

    time.sleep(1)