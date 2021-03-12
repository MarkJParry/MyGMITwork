#Filename:  numpyLab.py
#Author:    Mark Parry
#Created:   09/03/2021
#Purpose:   Weekly Lab 8 using numpy, demonstrates numpy array properties


import numpy as np

salMin = 20000
salMax = 80000
salLen = 10

#2. seeds the random numbers so that they stay the same while program is being run and tested
np.random.seed(1)

#1. program that makes a list, called salaries, that has (say 10) random numbers (20000 – 80000).
salaries = np.random.randint(salMin,salMax,salLen)
print(salaries)

#3. Adds a fixed amount to every item in the array
salaryBonus = salaries + 5000
print(salaryBonus)

#4. Increases every item in the array by a percentage increase

salaryIncrease = salaries * 1.05
print(salaryIncrease)


#5. converts the float items in the array to integers
intSalaryIncrease = salaryIncrease.astype(int)
print(intSalaryIncrease)

