"""Review question test 1 TPRG2131 Location class."""

### DEFINE CLASS LOCATION HERE ###
from math import radians, sin, cos, asin, sqrt, pi

class Location(object):
    def __init__(self,name,lat,long):
        self.name = name
        self.lat = lat
        self.long = long
        return

    def get_name(self):
        return self.name

    def get_latitude(self):
        return self.lat

    def get_longitude(self):
        return self.long

    def distance_to(self, other):
        RADIUS = 6367.0  # km

    # Convert degrees to radians for math module trig functions
        lat1 = radians(self.get_latitude)
        long1 = radians(self.get_longitude)
        lat2 = radians(other.get_latitude)
        long2 = radians(other.get_longitude)
    
    # difference in latitude, longitude
        dlon = long2 - long1
        dlat = lat2 - lat1
    # arc subtended by angle between two vectors origined at the centre
        a = sin(dlat/2.0)**2 + cos( lat1) * cos(lat2) * sin(dlon/2.0)**2
        c = 2.0 * asin( min( 1.0, sqrt(a)))
        self.distance_to= RADIUS * c
        return self.distance_to


### DO NOT EDIT ANYTHING UNDER THIS LINE! ###
# To run the test, run the file from Idle (F5 Run module)
# or from the CMD.EXE command line (DOS box) as
#   > python location.py
# If all goes well, you should see output that looks like this:
# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.001s
#
# OK
#
# In other words, all tests passed and there were no errors to report.
###
if __name__ == '__main__':

    # Import the testing framework (see Python standard library section 26.4)
    import unittest 
    # unittest main will use this class to run several tests
    # with Location objects.
    class TestLocationMethods(unittest.TestCase):
        def setUp(self):
            self.place1 = Location("Toronto", 43.651975, -79.381714)
            self.place2 = Location("Peterborough", 44.308127, -78.31604)

        def test_get_name(self):
            self.assertEqual(self.place1.get_name(), "Toronto")
            self.assertEqual(self.place2.get_name(), "Peterborough")

        def test_get_latitude(self):
            self.assertEqual(self.place1.get_latitude(), 43.651975)
            self.assertEqual(self.place2.get_latitude(), 44.308127)

        def test_get_longitude(self):
            self.assertEqual(self.place1.get_longitude(), -79.381714)
            self.assertEqual(self.place2.get_longitude(), -78.31604)

        def test_distance_to(self):
            self.assertEqual(round(self.place1.distance_to(self.place2), 2), 112.15)
            self.assertEqual(round(self.place2.distance_to(self.place1), 2), 112.15)

    # Run the tests that were just defined.
    unittest.main()
