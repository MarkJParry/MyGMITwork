#Filename:  sub.py
#Author:    Mark Parry
#Created:   06/02/2021
#Purpose:   reads in two numbers and subracts the first one from the second one.

#set up variables and read in numbers
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

#do the calulation
result = int(num1 - num2)

#print the result
print("Your first number was {} your second was {}, {} take away {} is equal to {}".format(num1,num2,num1,num2,result))