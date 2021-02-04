#Filename:  round.py
#Author:    Mark Parry
#Created:   03/02/2021
#Purpose:   Program to take in a float number and outputs an int rounded down, using the math module 
#           the math.floor() method rounds a number DOWN to the nearest integer

import math

inNum = float(input("Please enter a number "))
outNum = math.floor(inNum)
print("You entered {} and using the math module it floored it to: {}".format(inNum,outNum))