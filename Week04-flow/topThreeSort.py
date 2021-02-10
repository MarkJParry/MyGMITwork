#Filename:  topThreeSort.py
#Author:    Mark Parry
#Created:   08/02/2021
#Purpose:   generates 10 random numbers (0-100) , prints them out then prints them out in descending order.
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

#print the generated list
print(randomList)

#copy the list to a temporary list to use  while sorting
tempList=randomList.copy()  

#loop through the original list
for all in randomList:

    previousNum,biggestNum = 0,0


#   loop throught the temporary list to find largest number
    for randomNum in tempList:
        if randomNum > previousNum:
            biggestNum = randomNum
            previousNum = randomNum

#   when done remove the largest number from the temporay list
    tempList.remove(biggestNum)

#   append this number to the outgoing list
    outList.append(biggestNum)

print(outList)