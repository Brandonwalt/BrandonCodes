"""my Greenhouse file created by Brandon Walters "finished" on 3/3/2017"""
import time
import datetime
import sys
import glob
development_mode = False
"""start of the development_mode"""
W1_BASE_DIR = "/sys/bus/w1/devices/"
try:
    import RPi.GPIO as GPIO
except ImportError as gpio_exception:
    print("Cannot import module {}, running in development mode."
          .format(gpio_exception.name), file=sys.stderr)
    development_mode = True
    import random
"""a try import happens so if the raspberry pi is
connected it will start to read from the txt file
if on windows then will trigger a ImportError
and run in Deveplor mode and insert a random number """
def gpio_setup(mode="BCM"):
    """when doing setup it will read if it set in to BCM but if not will just pass"""
    if mode == "BCM":
        GPIO.setmode(GPIO.BCM)
        return
    else:
        pass

def gpio_cleanup():
    """cleanup normall would clear the pins but since the code
was manly made on windows to cause less error will just pass"""
    pass

def read_ds18b20_config(file_name):
    """creates the file name for each senser"""
    file_name = self_id +" ID Name: " + self_name
    return file_name

def w1_enumerate(pin_number):
    """gives information the information from the device folder from the txt file
but of in developer mode will just return the first name and number"""
    if not development_mode:
        pin_number = glob.glob(base_dir +'28*')
        return pin_number
    else:
        return {"0001":"north", "0002":"centre"}

class Sensor(object):
    """start of the generic senser were it will send out information it gains from the sensers"""
    _sensor_type = "generic"
    _units = ""

    def __init__(self, _sensor_type, _units):
        self._sensor_type = _sensor_type
        self._units = _units
        return

    def Sensor(self, sensor_name, self_name):
        """defines sensor name as the self_name"""
        sensor_name = self_name
        return

    def get_type(self):
        """return self type gained from near the which sensor it reading"""
        return self._type

    def get_name():
        """returns the name of the sensor gained from the sensor txt file"""
        return sensor_name

    def get_units(self):
        """return units gained from near the which sensor it reading"""
        return self._units

    def read(self):
        """another developer mode trick when trying to
read if not in development mode it will
read then through the measuremnt file but if in the mode
will skip it and go throught the test setups"""
        if development_mode:
            reading = self._test_read()
        else:
            reading = self._hardware_read()
            return Measurement(reading, self._units)
        return _hardware_read

    def _test_hardware_setup(self):
        print("Initializing {}.".format(self._sensor_type), file=sys.stderr)
        return

    def _test_read(self):
        return 0

    def _hardware_read(self):
        _hardware_read = 0
        return _hardware_read

class SwitchSensor(Sensor):
    """create the readings for the switch sensor which is used to see if the sensor is on or off"""
    _sensor_type = "switch"
    _units = ""

    def __init__(self, sensor_name, pin_number):
        self._name = sensor_name
        self.pin_number = pin_number
        return

    def _hardware_setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_number, GPIO.IN)
        SwitchStatus = GPIO.input(self.pin_number)
        return SwitchStatus

    def _hardware_read():
        if SwitchStatus == 1:
            _hardware_read = 1
            return Sensor._hardware_read
        else:
            _hardware_read = 0
            return Sensor._hardware_read

class DS18B20Sensor(Sensor):
    """tempature sensor class used to define the tempature for the sensor in cealces"""
    _sensor_type = "ds18b20"
    _units = "C"  # degrees C

    def __init__(self, sensor_name, device_id):
        self.sensor_name = sensor_name
        self.device_id = device_id
        return

    def _file_path():
        _file_path = W1_BASE_DIR + self.device_id +'/w1_slave'
        return _file_path

    def _hardware_setup():
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def _hardware_read():
        lines = _hardware_setup()
        while lines[0] .strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                _hardware_read = temp_c
                return Sensor._hardware_read

class Measurement(object):
    """start of the measurment class used to combind the information gaind
from the tempature senser and send it out as a string statemint,
it also gives a timebase for the measurment when exported"""
    def __init__(self, _id, data, units=""):
        self._data = data
        self._id = _id
        self._units = units
        return

    def get_id(self):
        """ grabs the id so it can be sent for the string file """
        return self._id

    def get_data(self):
        """sends the data recaved from the sensor file """
        return self._data

    def get_units(self):
        """sends the units for the measurement __init__ which is blank"""
        return self._units

    def get_time(self):
        """creat the time that happeing right now and sending as _time"""
        _time = datetime.datetime.now()
        return _time

    def get_timestamp(self):
        """creates a string with the total date useing
the time gained from the get_time defanison"""
        _timestamp = _time.strftime("%Y/%m/%d 5H:%M:%S")
        return _timestamp

    def __str__(self):
        outstring = str(self.id)+" "+float(self.data)+" "+str(self._units)+" "+str(_timestamp)
        return outstring
