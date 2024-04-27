"""Suggested test code for the greenhouse.py module.

TPRG 2131 Winter 2017 Project 1.
Python 3.4 on Raspberry Pi
Louis Bertrand <louis.bertrand@durhamcollege.ca>
January 29, 2017
"""

from greenhouse import *

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
        #assert False, "Got here at finally"
        gpio_cleanup() # clean exit, reset the pins to inputs

    # Test the DS18B20Sensor class
    # In test mode, you can use a hard-coded dictionary of id:name pairs
    device_ids = {"0001":"north", "0002":"centre"}
    #device_ids = read_ds18b20_config("sensorsconfig.txt")
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

