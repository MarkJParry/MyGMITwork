#Filename:  normalise.py
#Author:    Mark Parry
#Created:   03/02/2021
#Purpose:   Program to read a string normailse it by removing leading and trailing spaces converting to lower case 
#           and also output the length of the input and output strings

#set up input string and get its length
inStr = input("Please enter a string with spaces before and after it with a mix of upper and lower case letters: ")
inStrLen = len(inStr)

#set up output string using strip() which removes the leading and trailing space from the input string and lower() which converts it to lower case and then get its length
outStr = inStr.strip().lower()
outStrLen = len(outStr)

#output both strings and their lengths
print("You entered {} which is {} characters long\nthe nomalised string {} is {} characters long.".format(inStr,inStrLen,outStr,outStrLen))