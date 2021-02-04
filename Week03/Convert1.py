#Filename:  convert1.py
#Author:    Mark Parry
#Created:   03/02/2021
#Purpose:   simplified program  that takes in a float amount of dollars, and returns that absolute amount in cent.

inAmount = float(input("Please enter the amount to convert in dollars and cents : "))

cents = round(abs(inAmount*100))

print("{} dollars is equivalent to {} cents in absolute terms".format(inAmount,cents,))
