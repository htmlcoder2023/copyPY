import os
inputfile = input("Input File: ")
outputfile = input("Output File: ")
print(inputfile + " size: " + str(os.path.getsize(inputfile)))
fileSizeRead = int(input("File size read: "))
startingAddr = int(input("Starting byte address: "))
inputfile = open(inputfile, "rb")
inputfile.seek(startingAddr)
inputfile = inputfile.read(fileSizeRead)
outputfile = open(outputfile, "wb")
outputfile.write(inputfile)
outputfile.close()