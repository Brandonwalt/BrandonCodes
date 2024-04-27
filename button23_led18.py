"""Blink the LED on GPIO 18.

Louis Bertrand <louis.bertrand@durhamcollege.ca>
Jan 16, 2017
Platform: Raspberry Pi + Python 3

Simple button-lED example for TPRG2131 Winter 2017
"""


class ButtonSensor(object):
    """Model a pushbutton switch."""
    def __init__(self, pin_number):
        """Create a new instance and enable pin."""
        self._pin = pin_number
        GPIO.setup(pin_number, GPIO.IN)
        return

    def read(self):
        """Read the pin."""
        if GPIO.input(self._pin):
            return True
        else:
            return False


import RPi.GPIO as GPIO # pylint: disable=import-error

GPIO.setmode(GPIO.BCM)  # Broadcom chip pin numbering

LED_PIN = 18  # prefer to use names
BUTTON_PIN = 23
BLINK_DELAY = 0.2  # seconds per half cycle

# Hardware setup
GPIO.setup(LED_PIN, GPIO.OUT)

button1 = ButtonSensor(BUTTON_PIN)

try:
    while True:
        if button1.read():
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

except KeyboardInterrupt:
    print("CTRL-C received, exiting...")
# Catch all other exceptions to ensure the reset happens.
except Exception as something:  # pylint: disable=broad-except
    print("Unknown exception caught:\n", something, "\nexiting...")
finally:
    GPIO.cleanup() # clean exit, reset the pins to inputs
