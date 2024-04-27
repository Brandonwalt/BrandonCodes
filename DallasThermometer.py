"""One or more DS18B20 thermal sensors on the Raspberry Pi.

Louis Bertrand <louis.bertrand@durhamcollege.ca>
Jan 18, 2017
Platform: Raspberry Pi + Python 3
TPRG 2131 Winter 2017

The program must be run as root to access the files in devfs.
The test:
 -- Identify one or more directories matching 28-*
 -- Determines a file path for each w1_slave file
 -- Attempts to read from each thermometer in a loop
 -- CTRL-C to exit.
For a more complete test, there should be at least two devices on the bus.
"""

# Main program test routine (not executed if loaded as a module)
if __name__ == "__main__":
    # pylint: disable=invalid-name
    # disable warning for variables in global (module) scope.
    import os
    import glob
    import time

    os.system("modprobe w1-gpio")
    os.system("modprobe w1-therm")

    base_dir = "/sys/bus/w1/devices/"
    dev_dirs = glob.glob(base_dir + "28*")
    sensors = []  # empty list of sensors and file paths to poll
    for dr in dev_dirs:
        print(dr)  # just to check the directory names
        parts = dr.rsplit("-")
        ident = parts[1]
        sensor_file = base_dir + "28-" + ident + "/w1_slave"
        sensor = (ident, sensor_file)
        sensors.append(sensor)
    # now that we have a list of sensors, poll them
    try:
        while True:
            for sn in sensors:
                temp_c = -999.0  # default answer
                # routine to read and parse the w1_slave file.
                infile = open(sn[1])
                lines = infile.readlines()
                infile.close()
                # reading valid?
                if lines[0].find("YES") != -1:
                    equals_pos = lines[1].find("t=")
                    if equals_pos != -1:
                        temp_string = lines[1][equals_pos + 2 :]
                        temp_c = float(temp_string) / 1000.0
                print(sn[0], temp_c)
                time.sleep(2) # poll every two seconds
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")
