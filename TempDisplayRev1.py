#Temperature Monitor Program Rev 1

import Adafruit_CharLCD as LCD
import os
import glob
import time
import datetime

lcd = LCD.Adafruit_CharLCDPlate()
lcd.clear()

lcd.message('Temperature \nMonitor Rev1')
time.sleep(2)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir +'28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

print('Press Ctrl-C to quit.')

try:
        while 1:
            lines = read_temp_raw()
            while lines[0].strip()[-3:] != 'YES':
                    time.sleep(0.2)
                    lines = read_temp_raw()
            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                temp_f = temp_c * 9.0 / 5.0+ 32.0
                lcd.home()
                now=datetime.datetime.now()
                lcd.message(now.strftime('%b %d  %H: %M: %S:\n'))
                lcd.message('\n%.1f' % (temp_c)+' C')
                lcd.message('  %.1f' % (temp_f)+' F')
                time.sleep(0.5)

except KeyboardInterrupt:
       print('Exiting Program....')
       lcd.clear()
       lcd.message('Exiting Program')
       time.sleep(1)
       lcd.clear()
       lcd.message('Temperature Program\nNot Running')
                    
