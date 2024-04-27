import math
def getFileName():
    ### allows user to pick the file but is also set that blank is also exceptal 
    file = input("Hello, please enter file's name: ")
    if file == "":
        file = "coordinates.txt"
    return file
    
def getFileHandle(filename):
    # start the function here
    handle = open(filename)
    return handle

def loadPlaceNames(inputfile):
    ### see's if file works and loads it in 
    files = []
    for line in inputfile:
        x = parseLine(line)
        if x != None:
            files.append(x)
    return files 

def parseLine(line):
    splitname = line.split(" ")
    if len (splitname) >= 3:        #splits the text file into 3 parts
        name = splitname [0]        #the first grouping of letters is split into a variable designated as name
        lat = splitname [1]         #the second variable is set as the latitude value
        long = splitname [2]        #the third variable is longitude variable
        if isfloatable(lat) and isfloatable(long):
            xlat = float(lat)           #the latitude variable is then redefined as a float
            xlong = float (long)        #the longitude variable is then redefined as a float
            if -90 <= xlat <= 90 and -180 <= xlong <= 180:     #when the latitude is equal to or greater than -90, and less than or equal to 90
                return name, xlat, xlong

def printList(plist):
    ordinal = 1
    for p in plist:
        print("{} {}".format(ordinal, p[0]))
        ordinal += 1
    print("0 for either number will exit the program.")
    return

def getChoice():
    area1 = input("first location ")   ### first choice for the user to select which place from the 8
    area2 = input("secound location ") ### secound choice
    places = tuple((area1, area2))
    return places

def haversine(area1, area2): ### the mathematics code to caculate the two locations
    xlon = area1[1]
    xlat = area1 [0]
    lon = area2 [1]
    lat = area2[0]
    dlon = xlon - lon 
    dlat = xlat - lat
    R = 6367
    a = math.sin(dlat/2.0)**2 + math.cos(xlon) * math.cos(xlat) * math.sin**2(dlon/2.0)**2
    c = 2 * math.asin(min(1,math.sqrt(a))) 
    d = R * c
    return d

    
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

    namelist = loadPlaceNames(file)
    print(namelist)
    while True:
        print(namelist)
        choice = getChoice()
        if int(choice[0]) == 0 or int(choice[1]) == 0:
            print ("closing program")
            time.sleep(10)
            break
        place1 = namelist[int(choice[0]) - 1]
        place2 = namelist[int(choice[1]) - 1]
        distance = haversine((place1[1], place1[2]), (place2[1], place2[2]))
        string1 = ('The distance between' +place1+ ' and ' +place2+ ' is ' +distance+ '.')
        print(string1)
        print("Done!")
        
