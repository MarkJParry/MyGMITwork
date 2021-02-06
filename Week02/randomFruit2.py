#Filename:  randomFruit2.py
#Author:    Mark Parry
#Created:   06/02/2021
#Purpose:   Prints out a random fruit using a different method random.choice
#Research:  askpython website
#           Generate Random Integers
#           The random module provides some special methods for generating random integers.
#           2. random.choice(seq)
#           Returns a randomly selected choice from a list

import random

#set up list with 5 fruits, a list of vowels and initialise the article for the output
fruits = ("apple","orange","banana","grape","kiwi")
vowels = ("a","e","i","o","u")
article = "a"

#generate a random choice from the list
fruit = random.choice(fruits)

#check if the randomly returned fruit starts with a vowel
if fruit[0] in vowels:
    article = "an"

print("A random fruit from this list: {} is {} {}".format(fruits,article,fruit) )
