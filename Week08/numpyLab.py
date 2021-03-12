#Filename:  numpyLab.py
#Author:    Mark Parry
#Created:   09/03/2021
#Purpose:   Weekly Lab 8 using numpy, matplotlib
#1. program that makes a list, called salaries, that has (say 10) random numbers (20000 – 80000).

import numpy as np
np.random.seed(1)
salMin = 20000
salMax = 80000
salLen = 10

salaries = np.random.randint(salMin,salMax,salLen)
print(salaries)
salaryBonus = salaries + 5000
print(salaryBonus)
salaryIncrease = salaries * 1.05
print(salaryIncrease)
intSalaryIncrease = salaryIncrease.astype(int)
print(intSalaryIncrease)

