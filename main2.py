"""Main program for the greenhouse Project part 2.

TPRG 2131 Winter 2017 Project 2.
Python 3.4 on Raspberry Pi
Louis Bertrand <louis.bertrand@durhamcollege.ca>
March 31, 2017
"""

# System modules
import time

# Project modules (must be in same folder or directory)
from greenhouse2 import *
from database2 import *

# Main program starts running here

print("development_mode",development_mode)

# Set up the GPIO; Does not touch hardware if development_mode==True
gpio_setup("BCM")  # set up GPIO pin numbering

# Test the switch sensor
sw1 = SwitchSensor("your_name_here SW1", 23)
print("sw1 is", sw1)
print("name", sw1.get_name(), " type", sw1.get_type())
status = sw1.read()
print(status, status.get_data(), status.get_timestamp())

sw2 = SwitchSensor("your_name_here SW2", 18)
print("sw2 is", sw2)
print("name", sw2.get_name(), " type", sw2.get_type())
status = sw2.read()
print(status, status.get_data(), status.get_timestamp())

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

# Print out details of each ds18b20 thermometer.
for t in therm_list:
    print("thermometer: ", t)
    print("name", t.get_name(), " type", t.get_type())
    status = t.read()
    print(status, "\n{:.3f}{}".format(status.get_data(), status.get_units()), status.get_timestamp())

# Begin storing measurements in the database
# Step 1: register each sensor in the units, type and sensor tables
#         This is necessary because of the primary key / foreign key
#         relationship. You can't refer in type to a units row that
#         doesn't exist yet
# Step 2: Take measurements at regular intervals and write them to the database.

# Open the database.
# The return value is a DatabaseConnector instance that translates high level
#  requests like "register sensor" and "store measurement" into specific sequences
#  of actions in Python and SQL queries.
# This is where a different database could be requested
#db = DatabaseConnector("measurement.db")
db = PostgreSQLConnector(dbname="greenhouse2", \
                       host="fluffy.durhamcollege.org", user=" brandonwalters1", \
                       password="thole-pippin-reborn-guppy")


# Register the thermometers
for therm in therm_list:
    db.register_sensor(therm)

# Register the switch sensors
#  Modify this list according to the sensors in your system.
db.register_sensor(sw1)
db.register_sensor(sw2)

# Read the sensors in the system every two seconds.
try:
    while True:
        # read the temperatures
        for therm in therm_list:
            db.store_measurement(therm.read())
        # read the switch sensors
        db.store_measurement(sw1.read())
        db.store_measurement(sw2.read())
        time.sleep(2.0)

except KeyboardInterrupt: 
    print("KeyboardInterrupt received\n   exiting...")
finally:
    gpio_cleanup() # clean exit, reset the pins to inputs

