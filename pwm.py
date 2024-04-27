import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED = 24
def setup():
    global pwm
    GPIO.setup (LED, GPIO.OUT)
    pwm = GPIO.PWM(LED, 200)
    pwm.start(100)
def set_brightness (new_brightness) :
    pwm.ChangeDutyCycle (new_brightness)
def flicker():
    set_brightness(random.randrange(0,100))
    time.sleep(random.randrange(1,10) * 0.01)
def loop():
    try:
             while True:
                 flicker()
    except KeyboardInterrupt:
             pass
    finally:
             GPIO.cleanup()
setup()
loop()
