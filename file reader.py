import linecache

print("Opening and closing the file.")
text_file = open("coordinates.txt", "r")
text_file.close()

print("\nReading characters from the file.")
        print(lines)
        print(len(lines))
        for line in lines:
            print(line)
        line = linecache.getline("coordinates.txt", 6)
    namelist = loadPlaceNames(file)
    lines = text_file.readlines()
