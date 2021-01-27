#Filename:  addOne.py
#Author:    Mark Parry
#Created:   27/01/2021
#Purpose:   Read in a number and add one to it and print the answer

numIn = input("Please enter a number: ")
numOut = int(numIn) + 1
print("{} is one more than the number you entered which was {}".format(numOut,numIn))