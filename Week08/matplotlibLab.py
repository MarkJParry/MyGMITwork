#Filename:  matplotlibLab.py
#Author:    Mark Parry
#Created:   09/03/2021
#Purpose:   Weekly Lab 8 using matplotlib, demonstrates how to use it

#5. Write a program that plots the function y = x**2.


import matplotlib.pyplot as mpl

import numpy as np

#Plot
xvalues = np.array(range(1,101))
yvalues = xvalues * xvalues 

mpl.plot(xvalues,yvalues)
mpl.show()


#hist
salMin = 20000
salMax = 80000
ageMin = 21
ageMax = 65
arrLen = 100

#2. seeds the random numbers so that they stay the same while program is being run and tested
np.random.seed(1)

#1. program that makes a list, called salaries, that has (say 10) random numbers (20000 – 80000).
salaries = np.random.randint(salMin,salMax,arrLen)


mpl.hist(salaries)
mpl.show()

#scatter
ages = np.random.randint(ageMin,ageMax,arrLen)

mpl.scatter(ages, salaries)

mpl.show()

#mixed
mpl.scatter(ages, salaries, label="Salaries")
mpl.plot(xvalues,yvalues,color="r", label="x squared")
mpl.title("random plot") 
mpl.xlabel("Salaries") 
mpl.ylabel("age") 
mpl.legend() 




mpl.savefig("prettier-plpt.png")
