#Filename:  round.py
#Author:    Mark Parry
#Created:   03/02/2021
#Purpose:   Program to take in a float number and round it up or down in integer format

inNum = float(input("Please enter a number with sign and some decimal places ie. -22.995  : "))
print("{} is rounded to {}".format(inNum,round(inNum)))