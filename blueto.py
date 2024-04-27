#Serial Write to tablet using a P3 - Phil J 14-6-16
#used the hardware Rx & Tx pins, cross linked to JY-MCU model
#Simple tablet coms test. (note used to the JY-MCU @ 4800bps)
#White to TXD, Green to RXD
import time
import serial
import os
#port='/dev/ttyAMA0' - OLD for P1 & P2
##ser = serial.Serial(
## port='/dev/serial0',
## baudrate = 4800,
## parity=serial.PARITY_NONE,
## stopbits=serial.STOPBITS_ONE,
## bytesize=serial.EIGHTBITS,
## timeout=1
##)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 4800,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,timeout=1
)
counter=0
print("Serial is open: "+str(ser.isOpen()));
while 1:
    res = os.popen('vcgencmd measure_temp').readline()
    vol = os.popen('vcgencmd measure_volts $id').readline()
    print("Core temp: "+str(res));
    print("B.W & A.S");
    ser.write('Write counter: %d \n'%(counter))
    ser.write('Core Temp: = '+(res))
    print("Core Voltage: "+str(vol));
    ser.write('Voltage: = '+(vol))
    time.sleep(1)
    counter = counter + 1
    print counter
    
