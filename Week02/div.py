#Filename:  div.py
#Author:    Mark Parry
#Created:   06/02/2021
#Purpose:   Reads in two numbers and divides the first one by the second and give the integer result and the remainder.

#set up variables and read in numbers
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

#do the calulation
result = int(num1 / num2)
remainder = int(num1 % num2)
if num2 > num1:
    result = float(num1 / num2)
    remainder = 0

#print the result
print("Your first number was {} your second was {}, {} divided by {} is equal to {} remainder {}".format(num1,num2,num1,num2,result,remainder))
