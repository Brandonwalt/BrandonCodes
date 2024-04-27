import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23,GPIO.IN)
input = GPIO.input(23)

while True :
    if (GPIO.input(23)):
        print("Button is Pressed")
