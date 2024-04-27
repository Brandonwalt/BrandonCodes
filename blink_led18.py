"""Blink the LED on GPIO 18.

Louis Bertrand <louis.bertrand@durhamcollege.ca>
Jan 16, 2017
Platform: Raspberry Pi + Python 3

Simple example for TPRG2131 Winter 2017
"""

import time
import RPi.GPIO as GPIO # pylint: disable=import-error

GPIO.setmode(GPIO.BCM)  # Broadcom MCU pin numbering

LED_PIN = 18  # prefer to use names
BLINK_DELAY = 0.2  # seconds per half cycle

GPIO.setup(LED_PIN, GPIO.OUT)

try:
    # Disable because PyLint treats module-level variables as constants;
    # clearly, led_state is not a constant and should be lowercase.
    # pylint: disable=invalid-name
    led_state = True
    while True:
        GPIO.output(LED_PIN, led_state)
        led_state = not led_state
        time.sleep(BLINK_DELAY)

except KeyboardInterrupt:
    print("CTRL-C received, exiting...")
except Exception as oops: # pylint: disable=broad-except
    print("Unknown exception caught -- ", oops, " --, exiting...")
finally:
    GPIO.cleanup() # clean exit, reset my pins to inputs
