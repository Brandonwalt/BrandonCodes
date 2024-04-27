#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import Adafruit_GPIO.SPI as SPI 
import Adafruit_MCP3008
import serial
import os.path

##import picamera


 
#GPIO SETUP
CLK  = 18 
MISO = 23 
MOSI = 24 
CS   = 25 
Pump = 17
Mosture = 2
Servo_Motor = 3
Power_Sensor = 17
Water_Pump = 27
Lights = 4
Temp_Sensor = 18
Heater = 22

Low_level = 2
High_Level = 700
Light_level = 300
Temp_level = 20

##camera = picamera.PiCamera()
# setting the monoter pins
auto_mode = True

##def Values():
##  values_0 = mcp.read_adc(0)  # ADC vaule for mosture sensor
##  values_1 = mcp.read_adc(1)  # ADC vaule for Photoresister average
##  values_2 = mcp.read_adc(2)  # ADC vaule for tempature sensor
##  values_3 = mcp.read_adc(3)  # ADC vaule for voltage monitor
##  values_4 = mcp.read_adc(4)  # ADC vaule for water flow meter
##  return values_0, values_1, values_3, values_4

  


def mode():
  if ser.read(4) == "On":
    auto_mode = True
    return auto_mode
  else:
    if ser.read(4) == "Off":
      auto_mode = False
      return auto_mode


##def output(values_0, values_1, values_2 ,values_3, vaules_4):
##  ser.write("mosture sensor" + values_0 + "\n")
##  ser.write("Photoresister average" + values_1 + "\n")
##  ser.write("tempature sensor" + values_2 + "\n")
##  ser.write("Power monitor" + Power1 + "\n")
##  ser.write("water flow meter" + values_4 + "\n")
##  return
  
##def Open_window(Self):
##    p.ChangeDutyCycle(7.5)
##    return
##
##def Close_window(Self):
##    p.ChangeDutyCycle(2.5)
##    return

  
while True:

  # GPIO Setup for each pin
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(Mosture, GPIO.IN)
  GPIO.setup(Light_level, GPIO.IN)
  GPIO.setup(Power_Sensor, GPIO.IN)
  GPIO.setup(Servo_Motor, GPIO.OUT)
  GPIO.setup(Lights, GPIO.OUT)
  GPIO.setup(Water_Pump, GPIO.OUT)
  GPIO.setup(Temp_Sensor, GPIO.IN)
  GPIO.setup(Heater, GPIO.OUT)
  p = GPIO.PWM(Servo_Motor, 50)
  p.start(7.5)


  ser = serial.Serial(   
      port='/dev/ttyUSB0',
      baudrate = 19200,
      parity=serial.PARITY_NONE,
      stopbits=serial.STOPBITS_ONE,
      bytesize=serial.EIGHTBITS,
      timeout=1
  )

  
  mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
  values_0 = mcp.read_adc(0)  # ADC vaule for mosture sensor
  values_1 = mcp.read_adc(1)  # ADC vaule for Photoresister average
  values_2 = mcp.read_adc(2)  # ADC vaule for tempature sensor
  values_3 = mcp.read_adc(3)  # ADC vaule for voltage monitor
  values_4 = mcp.read_adc(4)  # ADC vaule for water flow meter

  Power1 = values_3 * 5

  ms = int(values_0)
  pa = int(values_1)
  ts = int(values_2)
  pm = int(Power1)
  wfm = int(values_4)
  

  save_path = '/home/pi/Desktop/codes'
  completeName = os.path.join(save_path,"ADC values"+".txt")

  time.sleep(1)

  x = ("mosture sensor " + str(ms) + "\n")
  
  out_file = open(completeName, "wt")
  out_file.write("mosture sensor " + str(ms) + "\n")
  out_file.write("Photoresister average " + str(pa) + "\n")
  out_file.write("tempature sensor " + str(ts) + "\n")
  out_file.write("Power monitor " + str(pm) + "\n")
  out_file.write("water flow meter " + str(wfm) + "\n")
  out_file.close()

##  if values_0 <= 212:
##    ser.write("mosture sensor 1V \n")
##  elif values_0 >= 213 and values_0 <= 424:
##    ser.write("mosture sensor 2V \n")
##  elif values_0 >= 425 and values_0 <= 700:
##    ser.write("mosture sensor 3.3V \n")
##  elif values_0 > 700:
##    ser.write("mosture sensor 5V \n")
##  else:
##    ser.write("mosture sensor 0V \n")
  

##  ser.write("mosture sensor " + str(ms) + "\n")
##  ser.write("Photoresister average " + str(pa) + "\n")
##  ser.write("tempature sensor " + str(ts) + "\n")
##  ser.write("Power monitor " + str(pm) + "\n")
##  ser.write("water flow meter " + str(wfm) + "\n")

  if auto_mode == True:
    Setting = "Auto mode is on"
    Print("____________________________")
    if values_0 >= Low_level and values_1 >= Light_level and values_2 >= Temp_level and values_0 < High_Level and values_2 < High_Level:
      GPIO.output(Water_Pump, GPIO.HIGH)
      GPIO.output(Lights, GPIO.HIGH)
      GPIO.output(Heater, GPIO.HIGH)
      p.ChangeDutyCycle(2.5)
      print("All off")
      print(Setting)
    elif values_0 >= Low_level and values_1 >= Light_level and values_2 <= Temp_level and values_0 < High_Level and values_2 < High_Level:
      GPIO.output(Water_Pump, GPIO.HIGH)
      GPIO.output(Lights, GPIO.HIGH)
      GPIO.output(Heater, GPIO.HIGH)
      p.ChangeDutyCycle(7.5)
      print("temp on")
      print(Setting)
    elif values_0 >= Low_level and values_1 <= Light_level and values_2 >= Temp_level and values_0 < High_Level and values_2 < High_Level:
      GPIO.output(Water_Pump, GPIO.HIGH)
      GPIO.output(Lights, GPIO.HIGH)
      GPIO.output(Heater, GPIO.HIGH)
      p.ChangeDutyCycle(2.5)
      print("light on")
      print(Setting)
    elif values_0 >= Low_level and values_1 <= Light_level and values_2 <= Temp_level and values_0 < High_Level and values_2 < High_Level:
      GPIO.output(Water_Pump, GPIO.HIGH)
      GPIO.output(Lights, GPIO.HIGH)
      GPIO.output(Heater, GPIO.HIGH)
      p.ChangeDutyCycle(7.5)
      print("light and temp on")
      print(Setting)
    elif values_0 <= Low_level and values_1 >= Light_level and values_2 >= Temp_level and values_0 < High_Level and values_2 < High_Level:
      GPIO.output(Water_Pump, GPIO.HIGH)
      GPIO.output(Lights, GPIO.HIGH)
      GPIO.output(Heater, GPIO.HIGH)
      p.ChangeDutyCycle(2.5)
      print("Pump on")
      print(Setting)
    elif values_0 <= Low_level and values_1 >= Light_level and values_2 <= Temp_level and values_0 < High_Level and values_2 < High_Level:
      GPIO.output(Water_Pump, GPIO.HIGH)
      GPIO.output(Lights, GPIO.HIGH)
      GPIO.output(Heater, GPIO.HIGH)
      p.ChangeDutyCycle(7.5)
      print("Pump and temp on")
      print(Setting)
    elif values_0 <= Low_level and values_1 <= Light_level and values_2 >= Temp_level and values_0 < High_Level and values_2 < High_Level:
      GPIO.output(Water_Pump, GPIO.HIGH)
      GPIO.output(Lights, GPIO.HIGH)
      GPIO.output(Heater, GPIO.HIGH)
      p.ChangeDutyCycle(2.5)
      print("Pump and lights on")
      print(Setting)
    elif values_0 <= Low_level and values_1 <= Light_level and values_2 <= Temp_level and values_0 < High_Level and values_2 < High_Level:
      GPIO.output(Water_Pump, GPIO.HIGH)
      GPIO.output(Lights, GPIO.HIGH)
      GPIO.output(Heater, GPIO.HIGH)
      p.ChangeDutyCycle(7.5)
      print("All off")
      print(Setting)
    elif values_0 >= High_Level:
      GPIO.output(Water_Pump, GPIO.LOW)
      GPIO.output(Lights, GPIO.LOW)
      GPIO.output(Heater, GPIO.LOW)
      p.ChangeDutyCycle(7.5)
      print("Water Too High")
      print(Setting)
      auto_mode = False
    elif values_2 >= High_Level:
      GPIO.output(Water_Pump, GPIO.LOW)
      GPIO.output(Lights, GPIO.LOW)
      GPIO.output(Heater, GPIO.LOW)
      p.ChangeDutyCycle(7.5)
      print("Heat Too High")
      print(Setting)
      auto_mode = False
  else:
    Setting = "Auto mode is off"
    print(Setting)
    ser.write("Enter On to turn on Auto Mode \n")
    ser.write("Enter Off to turn off Auto Mode \n")
    ser.write("Enter Pump_On to turn on Pump \n")
    ser.write("Enter Pump_Off to turn off Pump \n")
    ser.write("Enter Heater_On to turn on Heater \n")
    ser.write("Enter Heater_Off to turn off Heater \n")
    ser.write("Enter LED_On to turn on URV LED \n")
    ser.write("Enter LED_Off to turn off URV LED \n")


    
      
