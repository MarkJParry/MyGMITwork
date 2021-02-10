#Filename:  gradeExtra.py
#Author:    Mark Parry
#Created:   08/02/2021
#Purpose:   reads in a students percentage mark and prints out corresponding the grade (the program should check that the percentage is valid:
# • Under 40% => Fail
# • Between 40% and 49% => Pass
# • Between 50% and 59% => Merit 2
# • Between 60% and 69% => Merit 1
# • Over 70% => Distinction

#Changed to account for practise of rounding up 69.5 to a distinction and to loop until -1 is entered before finishing

#set up markIn as the control varaible for loop
markIn = 0

while markIn != -1:
#obtain student percentage
    markIn = round(float(input("Please enter the students' percentage mark or -1 to exit: ")))
    if markIn == -1:
        print("You have chosen to terminate the program - goodbye")
        exit()


#check if it is a valid percentage ie between 0 and 100
    if markIn >= 0 and markIn <= 100:
        markIsValid = True
    else:
        markIsValid = False

#calculate the grade if valid otherwise output an error message
    if markIsValid:
        if markIn < 40:
            grade = "Fail"
        elif markIn < 50:
            grade = "Pass"
        elif markIn < 60:
            grade = "Merit 2"
        elif markIn <= 70:
            grade = "Merit 1"
        else:
            grade = "Distinction"
        print("The grade for a {}% mark is: {}".format(markIn,grade))
    else:
        print("You have entered an invalid mark - please try again by entering a number between 0 and 100")
