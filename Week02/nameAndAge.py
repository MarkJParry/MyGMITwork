#Filename:  nameAndAge.py
#Author:    Mark Parry
#Created:   27/01/2021
#Purpose:   Reads in user name and age and says thanks <name> and makes a comment on their <age>.

name = input("Hi - whats your name? ")
age = input("Nice to meet you {} how old are you? ".format(name))
print("Thanks {},\t {} is a good age!".format(name,age))