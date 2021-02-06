#Filename:  randomGenerator.py
#Author:    Mark Parry
#Created:   06/02/2021
#Purpose:   prints out a random number between 1 and 10
#Research:  askpython website
#           Generate Random Integers
#           The random module provides some special methods for generating random integers.
#           1. randrange(start, stop, step)
#           Returns a randomly selected integer from range(start, stop, step). This raises a ValueError if start > stop.


#import the random library
import random

#use randrange to generate the random number  add 1 to the range stop =>(counters index,range,loop,etc  start at 0) otherwise 10 will never be generated
result = random.randrange(1,11,1)

#print the result
print("Your random number between 1 and 10 is: {}".format(result))