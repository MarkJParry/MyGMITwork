#Filename:  week07Lab2.py
#Author:    Mark Parry
#Created:   04/03/2021
#Purpose:   Read from a file, write, check for existence, create

import os.path



def checkIfExists():
    if os.path.isfile(filename) == True:
        print("File Exists")
    else:
        print("File does not exist - creating it now")
        initCount(0)



def getCount():
    with open (filename,"rt") as infile:
        count = int(infile.read())
        return count

def updateCount(count):
    with open (filename,"wt") as infile:
        count = (infile.write(str(count + 1)))

def initCount(count):
    with open (filename,"wt") as infile:
        count = (infile.write(str(count)))

filename = "count.txt"

checkIfExists()

count = getCount()
print(count)
updateCount(count)
count = getCount()
if count > 1:
    plural = "s"
else:
    plural = ""


print("This program has been run {} time{}".format(count,plural))
