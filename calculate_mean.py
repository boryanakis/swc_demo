import sys

# read in the command line arguments
myFileName = sys.argv[1]
stateAbbr = sys.argv[2]
numYears = int(sys.argv[3])

# open file for reading
myFile = open(myFileName, "r")

# create lists to store the data
yearList = []
tempsList = []

# read in the data
for line in myFile:
    year, temp = line.rstrip().split(",")
    year = int(year)
    temp = float(temp)
    yearList.append(year)
    tempsList.append(temp)

# subset data
tempsToBeAveraged = tempsList[-numYears:]
yearsToBeAveraged = yearList[-numYears:]

# calculate mean
average = sum(tempsToBeAveraged)/len(yearsToBeAveraged)

# output
output = [stateAbbr, str(round(average, 2))]

# print mean
print("\t".join(output))

# close file
myFile.close()
