import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import time

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
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading
    
while True:
    print RCtime(12)
    if RCtime(12) <1000:
        GPIO.output(RED, True)
        GPIO.output(GREEN, False)
    elif RCtime(12) >1000:
        GPIO.output(RED, False)
        GPIO.output(GREEN, True)
    else:
        GPIO.output(RED, False)
        GPIO.output(GREEN, False)
