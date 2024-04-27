import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import time

GPIO.setup(25,GPIO.IN)
GPIO.setup(18,GPIO.OUT)
input = GPIO.input(25)

while True:
    if (GPIO.input(25)):
        print("Light Detected")
        time.sleep(0.2)
        GPIO.output(18,1)
        time.sleep(0.2)
        GPIO.output(18,0)
