#Filename:  guess2.py
#Author:    Mark Parry
#Created:   08/02/2021
#Purpose:   Prompts the user to guess a number, and keeps prompting the user to guess the number until the user gets the right.
#           modified version of guess1.py to tell  the user if there guess is too high or too low, each time they guess. 

#Initialse the number the user has to guess and a counter to count how many guesses
number = 9
count = 1

#Loop until user guesses correctly
guess = int(input("Please guess a number between 1 and 10: "))

while guess != number:
#check if guess igher or lower    
    if guess < number:
        hint = "It's Higher"
    else:
        hint = "It's Lower"

    guess = int(input("{} - guess again: ".format(hint)))
    count += 1

print("You guessed correctly - the number was {}, it took you {} goes.".format(guess,count))