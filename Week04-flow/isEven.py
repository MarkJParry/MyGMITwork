#Filename:  isEven.py
#Author:    Mark Parry
#Created:   08/02/2021
#Purpose:   Read in a number and determine if it is even or odd

numIn=int(input("Please enter a number: "))

if numIn % 2 == 0:
    print("{} is an even Number".format(numIn))
else:
    print("{} is an odd Number".format(numIn))