"""Support functions for geocoding application."""
#file getFileHandle( string filename)
import math
def getFileName():
    file = input("What is the file name?")
    if file == "":
        file = "coordinates.txt"
    return file
    
def getFileHandle(filename):
    # start the function here
    handle = open(filename)
    return handle

def loadPlaceNames(inputfile):
    files = []
    for line in inputfile:
        x = parseLine(line)
        files.append(x)
    return line

def parseLine(line):
    splitname = str.split(line)
    for x in line:
        t1 = splitname [0]
#        print(t1)
        t2 = float(splitname [1])
 #       print(t2)
        t3 = float(splitname [2])
     #   print(t3)
        try:
            if t1.isalpha():
                return t1
            else:
                return False
            if isfloatable(t2) & -90 <= t2 <= 90:
                return t2
            else:
                return False
            if isfloatable(t3) & -180 <= t2 <= 180:
                return t3
            else:
                return False
        except (ValueError, AttributeError):
            return False
        return t1, t2, t3

    
#def getChoice():

##def haversine(pair point 1, pair point 2):
##    dlon = lon2 - lon1 
##    dlat = lat2 - lat1
##    R = 6367
##    a = math.sin**2(dlat/2) + math.cos(lat1) * math.cos(lat2) * math.sin**2(dlon/2) 
##    c = 2 * math.asin(min(1,math.sqrt(a))) 
##    d = R * c 
    
def isfloatable(s):
    try:
        if s.isnumeric():
            return True
        else:
            x = float(s)
    except (ValueError, AttributeError):
        return False
    return True

if __name__== "__main__":
    file = getFileName()
    print(file)
    
    datafile = getFileHandle(file)
    if datafile == None:
        print ("could not open file")
    else:
        print("working")

    namelist = loadPlaceNames(datafile)
    print(namelist)
    

    formatname = parseLine(namelist)
    print(formatname)
