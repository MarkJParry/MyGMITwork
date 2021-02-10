#Filename:  topThree.py
#Author:    Mark Parry
#Created:   08/02/2021
#Purpose:   generates 10 random numbers (0-100) , prints them out then prints out the top three.
#Notes:     Tried this without looking at sorting methods, will look up these later to find better method, just wanted to try it out for myself

#use the random library 
import random

#initialise variables
randomNum,previousNum,biggestNum = 0,0,0
randomList,tempList,outList = [],[],[]


#generate a list of 10 random numbers using randrange and a for loop
for r in range(1,11):
    randomNum = random.randrange(0,101)
    randomList.append(randomNum)
    if randomNum > previousNum:
        biggestNum = randomNum
        previousNum = randomNum
print(randomList)
print(biggestNum)
outList.append(biggestNum)
for x in range(0,2):
    print(x)

    tempList=randomList.copy()
    tempList.remove(biggestNum)
    #print(tempList)
    
    previousNum,biggestNum = 0,0


    for randomNum in tempList:
        #print(randomNum)
        if randomNum > previousNum:
            biggestNum = randomNum
            previousNum = randomNum
    print(biggestNum)
    outList.append(biggestNum)
print(outList)