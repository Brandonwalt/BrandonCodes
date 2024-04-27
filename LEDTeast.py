GPIO_RED=18
GPIO_AMBER=23
GPIO_GREEN=24
TIME_AMBER=1
TIME_RED=2
TIME_GREEN=2
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup(GPIO_RED,GPIO.OUT)
GPIO.setup(GPIO_AMBER,GPIO.OUT)
GPIO.setup(GPIO_GREEN,GPIO.OUT)
while 1 :
    GPIO.output(GPIO_RED,False)
    GPIO.output(GPIO_AMBER,False)
    GPIO.output(GPIO_GREEN,True)
    time.sleep(TIME_GREEN)
    GPIO.output(GPIO_RED,False)
    GPIO.output(GPIO_AMBER,True)
    GPIO.output(GPIO_GREEN,False)
    time.sleep(TIME_AMBER)
    GPIO.output(GPIO_RED,True)
    GPIO.output(GPIO_AMBER,False)
    GPIO.output(GPIO_GREEN,False)
    time.sleep(TIME_RED)

