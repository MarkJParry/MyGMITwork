#Filename:  guess1.py
#Author:    Mark Parry
#Created:   08/02/2021
#Purpose:   Prompts the user to guess a number, and keeps prompting the user to guess the number until the user gets the right.

#Initialse the number the user has to guess and a counter to count how many guesses
number = 9
count = 1

#Loop until user guesses correctly
guess = int(input("Please guess a number between 1 and 10: "))

while guess != number:
    guess = int(input("Wrong - guess again: "))
    count += 1

print("You guessed correctly - the number was {}, it took you {} goes.".format(guess,count))