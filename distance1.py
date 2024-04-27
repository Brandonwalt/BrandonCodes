"""Calculate the distance between two places on Earth.

Author: Louis Bertrand <louis.bertrand@durhamcollege.ca>
Python version: 3.5.2
V 1.0 2017-01-04 Initial version

The program reads in a list of places from a text file,
one place per line as
<name> <latitude> <longitude>
 where
   name is a string without blanks or other punctuation,
   latitude is a decimal number between -90 and 90 (inclusive)
   longitude is a decimal number between -180 and 180 (inclusive)

After reading in a file (default name = coordinates.txt), the
program prompts the user to enter two places and calculates the
distance in kilometers using the haversine formula.
To exit, the user enters 0 for either choice.
"""

# import supporting functions from geofun module directly into the
# namespace of this program:
from geofun import getFileHandle, loadPlaceNames, getChoice, haversine


#string getFileName(void)
def getFileName():
    """Prompt the user for the name of the file containing the places.

    Returns a string containing the file name; takes no argument.
    If the user simply hits return, the function substitutes the default name:
    coordinates.txt
    Reference: https://docs.python.org/3.5/library/functions.html?highlight=input#input
    """

    filename = input("Name of places and coordinates file? ")
    if filename == "":
        filename = "coordinates.txt"
    return filename


#void printList(list places)
def printList(plist):
    """Prints the list of places, each name preceded by a number 1 to N.

    The first element of each item in the list is the place name. A counter
    starting at 1 keeps track of the number. The last line prints the
    reminder that 0 means end program.
    The str.format() method formats an output string according to format
    codes (similar to C printf() format codes):
    https://docs.python.org/3/library/stdtypes.html#str.format
    """
    ordinal = 1
    for p in plist:
        print("{} {}".format(ordinal, p[0]))
        ordinal += 1
    print("0 for either number will exit the program.")
    return


if __name__ == "__main__":
    #print startup greeting
    print("Great Circle distance calculator")

    #get file name from user
    fname = getFileName()
    print("Opening file {}".format(fname))

    #open the file
    coordFile = getFileHandle(fname)

    #read the file line by line and extract a list of place names and coordinates
    places = loadPlaceNames(coordFile)

    #while input is not zero
    while True:
        # print the list
        printList(places)
        # get the user's choice
        choice = getChoice()
        if int(choice[0]) == 0 or int(choice[1]) == 0:
            break # zero as a choice breaks out of loop

        # extract lat, long from choice and calculate the distance
        # get both items (adjust numbering back to zero start)
        place1 = places[int(choice[0]) - 1]
        place2 = places[int(choice[1]) - 1]
        distance = haversine((place1[1], place1[2]), (place2[1], place2[2]))

        # print the distance (the str.format() specifier limits to 2 decimals)
        print("The distance between {} and {} is {:.2f}km.\n".format(place1[0],\
            place2[0], distance))

    #print goodbye message
    print("Done!")
