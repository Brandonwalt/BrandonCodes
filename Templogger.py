import os
import glob
import time
import datetime

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
def read_temp ():
    lines = read_temp_raw()
    while lines[0] .strip()[-3:] != 'YES' :
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos !=-1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c, 

while True:
    f=open ('tempdata.txt','a')
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y/%m/%d 5H:%M:%S")
    outvalue = read_temp()
    outstring = str(timestamp)+"  "+str(outvalue)+"  C"
    print ("Writing "+outstring+" to tempdata.txt")

    f.write(outstring+"\n")
    f.close()
    
    time.sleep(3)
