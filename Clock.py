import Adafruit_CharLCD as LCD
import time 
import datetime
from subprocess import *

lcd = LCD.Adafruit_CharLCDPlate()

cmd = "ip -4 addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

def run_cmd (cmd):
	p = Popen (cmd, shell=True, stdout=PIPE)
	output = p.communicate()[0]
	return output
while 1:
	lcd.clear()
	now=datetime.datetime.now()
	ipaddr = run_cmd(cmd)
	lcd.message(now.strftime('%b %d  %H:%M:%S\n'))
	lcd.message("IP %s" % (ipaddr))
	time.sleep(2)
