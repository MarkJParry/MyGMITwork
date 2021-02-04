#Filename:  convert.py
#Author:    Mark Parry
#Created:   03/02/2021
#Purpose:   program  that takes in a float amount of dollars, and returns that absolute amount in cent.Plays with output format

import math

inAmount = float(input("Please enter the amount to convert in dollars and cents : "))
#get the absolute value if negative 
absAmount =abs(inAmount)
#drop the cents by flooring
dollars = math.floor(absAmount)
#drop the decimal point for the cents by mutlipying by 100
cents = round((absAmount - dollars)*100)
#add the dollars in cents to the cents
allCents = (dollars*100) + cents
print("{} dollars and {} cents is  equivalent to {} cents in absolute terms".format(dollars,cents,allCents))
