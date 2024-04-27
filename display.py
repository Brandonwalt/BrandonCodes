import time
import Adafruit_CharLCD as LCD
lcd = LCD.Adafruit_CharLCDPlate()
first = 'First Message'

lcd.message('Hello \nRPi')
time.sleep(5)
lcd.clear()
lcd.message(first)
time.sleep(5)
lcd.clear()
