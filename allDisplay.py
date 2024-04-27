import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import time 
import datetime
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
from subprocess import *

lcd = LCD.Adafruit_CharLCDPlate()


RED = 23
GREEN = 25
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.setup(RCpin, GPIO.IN)
    p = reading

    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

while True:
    lcd.clear()
    now=datetime.datetime.now()
    data = RCtime(12)
    lcd.message(now.strftime('%b %d  %H:%M:%S\n'))
    lcd.message("Photo Value %s" % (data))
    time.sleep(2)
    if RCtime(12) <1000:
        GPIO.output(RED, True)
        GPIO.output(GREEN, False)
    elif RCtime(12) >1000:
        GPIO.output(RED, False)
        GPIO.output(GREEN, True)
    else:
        GPIO.output(RED, False)
        GPIO.output(GREEN, False)  
