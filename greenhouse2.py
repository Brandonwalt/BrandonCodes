"""Greenhouse data collection system module."""

from datetime import datetime
import sys  #access to stderr and other system functions

# Module constants
W1_BASE_DIR = "/sys/bus/w1/devices/"  # 1-Wire devices in Linux devfs

# Determine if we are running on RPi or development system.
development_mode = False
try:
    import RPi.GPIO as GPIO
except ImportError as gpio_exception:
    print("Cannot import module {},"
          "running in development mode.".format(gpio_exception.name), file=sys.stderr)
    development_mode = True
    import random

def gpio_setup(mode="BCM") -> None:
    """Configure GPIO pin numbering."""
    if development_mode:
        pass  # nothing to do
    else:
        if mode == "BCM":
            GPIO.setmode(GPIO.BCM)  # Broadcom chip pin numbering
        elif mode == "GPIO":
            GPIO.setmode(GPIO.GPIO)  # GPIO connector pin numbering
        else:
            print("Invalid GPIO pin numbering mode; "
                  "must be BCM or GPIO.", file=sys.stderr)
    return


def gpio_cleanup() -> None:
    """Reset GPIO pins as inputs."""
    if development_mode:
        pass  # nothing to do
    else:
        GPIO.cleanup()
    return


def read_ds18b20_config(file_name) -> dict:
    """Read the ID:name pairs from the config file.
    Each line is "ID name" (name can be any string, to the end of line)."""
    config_file = open(file_name, "r")
    sensors = {}  # empty dictionary
    for line in config_file:
        line = line.strip()  # remove trailing blanks and newline
        parts = line.split(maxsplit=1)
        sensors[parts[0]] = parts[1]
    return sensors


def w1_enumerate(pin_number) -> list:
    """Enumerate the 28-* devices on the 1-Wire bus and return IDs."""
    if development_mode:
        return ["01234", "45678", "12312"]

    # need these modules
    import os
    import glob

    # Load kernel modules and probe for bus and devices
    os.system("modprobe w1-gpio") # GPIO -> 1-Wire
    os.system("modprobe w1-therm")  # 1-Wire -> DS18B20

    dev_dirs = glob.glob(W1_BASE_DIR + "28*")
    sensors = []  # empty list to be filled in
    for dr in dev_dirs:
        print(dr, file=sys.stderr)  # just to check the directory names
        parts = dr.rsplit("-")
        ident = parts[1]
        sensors.append(ident)
    return sensors


class Measurement(object):
    """Measurement data and time stamp."""
    def __init__(self, identification: str, data: float, units="") -> None:
        """Record the measurement and attach a time stamp."""
        self._id = identification
        self._data = data
        self._units = units
        self._timestamp = datetime.utcnow() # timestamp with microseconds
        return

    def get_id(self) -> str:
        """Return measurement indentification string."""
        return self._id

    def get_data(self) -> float:
        """Return measurement value."""
        return self._data

    def get_units(self) -> str:
        """Return measurement units."""
        return self._units
    
    def get_time(self) -> float:
        """Return measurement time stamp as seconds from the epoch."""
        return self._timestamp

    def get_timestamp(self) -> str:
        """Format time stamp as a ISO 8601 "yyyy-mm-dd HH:MM:SS.ssssss"."""
        return self._timestamp.isoformat(" ") # blank separator instead of 'T'

    def __str__(self) -> str:
        """Format a string "<id> <value> <units> <timestamp>."""
        return str(self._id) + " " + str(self._data) + " " + str(self._units) + " " + self.get_timestamp()


class Sensor(object):
    """Base class for data collection sensors."""
    _SENSOR_TYPE = "generic"
    _UNITS = ""  # generic sensor has no units

    def __init__(self, sensor_name: str) -> None:
        """Construct a generic sensor."""
        self._name = sensor_name
        return

    def get_type(self) -> str:
        """Accessor for sensor type."""
        return self._SENSOR_TYPE

    def get_name(self) -> str:
        """Accessor for sensor name."""
        return self._name

    def get_units(self) -> str:
        """Accessor for sensor name."""
        return self._UNITS

    def read(self) -> Measurement:
        """Read the sensor and return a Measurement instance."""
        if development_mode:
            reading = self._test_read()
        else:
            reading = self._hardware_read()
        return Measurement(self._name, reading, self._UNITS)

    def _test_hardware_setup(self) -> None:
        """Pretend to configure the sensor hardware."""
        print("Initializing {}.".format(self._SENSOR_TYPE), file=sys.stderr)
        return

    def _test_read(self) -> int:
        """Always returns a zero; meant to be overridden."""
        return 0


class SwitchSensor(Sensor):
    """Simple open/closed sensor."""
    _SENSOR_TYPE = "switch"
    _UNITS = ""  # switch sensor has no units (only on/off)

    def __init__(self, sensor_name: str, pin_number: int) -> None:
        """Construct a new switch sensor"""
        Sensor.__init__(self, sensor_name)
        self._pin = pin_number
        if development_mode:
            self._test_hardware_setup()
        else:
            self._hardware_setup()

    def _hardware_setup(self) -> None:
        """Configure the GPIO pin as an input."""
        GPIO.setup(self._pin, GPIO.IN)
        return

    def _test_read(self) -> int:
        """Returns 0 or 1 at random."""
        return random.randint(0,1)

    def _hardware_read(self) -> int:
        if GPIO.input(self._pin):
            sw_value = 1
        else:
            sw_value = 0
        return sw_value


class DS18B20Sensor(Sensor):
    """Read a DS18B20 thermometer chip on a shared 1-Wire bus."""
    _SENSOR_TYPE = "ds18b20"
    _UNITS = "C"  # degrees C

    def __init__(self, sensor_name: str, device_id: int) -> None:
        """Construct a new ds18B20 sensor"""
        Sensor.__init__(self, sensor_name)
        self._id = device_id
        if development_mode:
            self._test_hardware_setup()
        else:
            self._hardware_setup()

    def _hardware_setup(self) -> None:
        """Determine the w1_slave file path."""
        self._file_path = W1_BASE_DIR + "28-" + self._id + "/w1_slave"
        # attempt to open to read
        try:
            infile = open(self._file_path)
        except OSError as oops:
            print(oops, file=sys.stderr)
        infile.close()
        return

    def _test_hardware_setup(self) -> None:
        """set up a random number generator for fake readings."""
        import random
        self._gen = random.Random()
        return

    def _test_read(self) -> float:
        """Returns 25 plus or minus a random value, sigma=1."""
        return round(self._gen.gauss(25, 0.1),3)

    def _hardware_read(self) -> float:
        """Read the w1_slave file."""
        infile = open(self._file_path)
        lines = infile.readlines()
        infile.close()
        # reading valid?
        if lines[0].find("YES") != -1:
            equals_pos = lines[1].find("t=")
            if equals_pos != -1:
                temp_string = lines[1][equals_pos + 2 :]
                temp_c = float(temp_string) / 1000.0
        return temp_c


if __name__ == "__main__":
    try:
        gpio_setup("BCM")  # set up GPIO pin numbering

        # Test the switch sensor
        sw1 = SwitchSensor("window", 23)
        print("sw1 is", sw1)
        print("name", sw1.get_name(), " type", sw1.get_type())
        status = sw1.read()
        print(status, status.get_data(), status.get_timestamp())

        sw2 = SwitchSensor("door", 18)
        print("sw2 is", sw2)
        print("name", sw2.get_name(), " type", sw2.get_type())
        status = sw2.read()
        print(status, status.get_data(), status.get_timestamp())
    except Exception as something:  # pylint: disable=broad-except
        print("Unknown exception caught:\n", something, "\nexiting...")
    finally:
        gpio_cleanup() # clean exit, reset the pins to inputs

    # Test the DS18B20Sensor class
    # In test mode, w1_enumerate() returns a constant list of fake IDs:
    # "01234", "45678", "12312" which must be mentioned in the config file.
    device_ids = read_ds18b20_config("sensorsconfig.txt")
    therm_list = []  # list of thermometers
    for therm_id in w1_enumerate(4):
        try:
            device_name = device_ids[therm_id]
            therm_list.append(DS18B20Sensor(device_name, therm_id))
        except KeyError as not_found: 
            print("ID", not_found, "on 1-Wire bus not found in config file.", file=sys.stderr)
    
    for t in therm_list:
        print("thermometer: ", t)
        print("name", t.get_name(), " type", t.get_type())
        status = t.read()
        print(status, "\n{:.3f}{}".format(status.get_data(), status.get_units()), status.get_timestamp())














