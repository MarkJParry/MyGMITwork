#Filename:  randomFruit.py
#Author:    Mark Parry
#Created:   06/02/2021
#Purpose:   Prints out a random fruit

import random

#set up list with 5 fruits, a list of vowels and initialise the article for the output
fruits = ["apple","orange","banana","grape","kiwi"]
vowels = ["a","e","i","o","u"]
article = "a"

#generate a random number between 1 and 5 using random lib
#list indices start at 0 so make sure to subtract one from the number generated and add 1 to the last number in the range
index = int(random.randrange(1,6,1) -1) 
fruit = fruits[index]

#check if the randomly returned fruit starts with a vowel
if fruit[0] in vowels:
    article = "an"

print("A random fruit from this list: {} is {} {}".format(fruits,article,fruit) )
