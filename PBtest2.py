import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import time

GPIO.setup(23,GPIO.IN)
input = GPIO.input(23)

while True :
    if (GPIO.input(23)):
        print("Button is Pressed")
        time.sleep(0.2)
