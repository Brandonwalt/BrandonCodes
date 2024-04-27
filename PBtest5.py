import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import time

GPIO.setup(23,GPIO.IN)
GPIO.setup(18,GPIO.OUT)
input = GPIO.input(23)
a=1

while True :
    if (GPIO.input(23)):
        print("Button has been Pressed"),a,"times"
        time.sleep(0.2)
        if a==12:
           print("Dozen Compleated, Change Box")
           count = 0
           while count <3 :
               GPIO.output(18,1)
               time.sleep(0.2)
               GPIO.output(18,0)
               time.sleep(0.2)
               count=count+1
               a=0
        a=a+1
