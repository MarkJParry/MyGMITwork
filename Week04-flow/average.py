#Filename:  average.py
#Author:    Mark Parry
#Created:   08/02/2021
#Purpose:   Keeps reading numbers until the user enters a 0. prints out each of the numbers entered and the average of them.

#initialise variables
numIn = 1
numList = []
sumNumIn = 0
average = 0
count = 0
#loop until user inputs 0 to end
while numIn != 0:
    numIn =int(input("Please enter a number or 0 to finish: "))
    if numIn !=0:
        numList.append(numIn)       #add the number to the list
        count += 1                  #increment the count by 1 
        sumNumIn += numIn           #add the number to the sum of the numbers
        average = sumNumIn/count    #divide the sum of the numbers by the count of the numbers

#print the count , list of numbers and their average       
print("You entered {} numbers as follows {} their average is {}".format(count, numList, average))