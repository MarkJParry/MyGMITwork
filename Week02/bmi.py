#Filename:  bmi.py
#Author:    Mark Parry
#Created:   27/01/2021
#Purpose:   Read in users height and weight and return their bmi(body mass index)
#Formula:   weight (kg) / [height (m)]2  BMI is weight in kilograms divided by height in meters squared.

height = input("Please enter your height in centimetres: ")
weight = input("Please enter your weight in kilograms: ")

heightInMetersSquared = (int(height)/100)**2  #using int here to convert the inputted strings to integers so math can be performed
bmi = int(weight)/heightInMetersSquared 

print("Thanks - your BMI is {}".format(bmi))