#Filename:  studentManagement.py
#Author:    Mark Parry
#Created:   25/02/2021
#Purpose:   Program to add and view students.
# 
# 
#set up dict

studentDetails = {  "Student1":{
                                "Name":"Mary",
                                "Course":{
                                            "English":"A+",
                                            "Irish":"C-"
                                         },
                             },
                    "Student2":{
                                "Name":"Mark",
                                "Course":{
                                            "English":"A",
                                            "Irish":"C+",
                                            "Physics":"B+"
                                         },
                              }
                 }

for student, name in studentDetails.items():
    print(student, name)
    for course in courses.item():
            print(course)

#define menu, add and view functions
def doMenu():
    option = input("Please choose from the following options:\n[a] Add a New Student\n[v] View an Existing Student\n[q] Quit\nType the letter a, v or q ").strip()
    return option

def doAdd():
    print("In Add")
    aName = "InAdd"
    while (aName != ""):
        aName = input("Enter the name of the student you would like to add:\nLeave this blank to return to the menu ").strip()

def doView():
    print("In View")
    vName = "InView"
    while (vName != ""):
        vName = input("Enter the name of the student you would like to view:\nLeave this blank to return to the menu ").strip()
        print(studentDetails.get(vName))

#start
choice = ""
while (choice != "q"):
    choice = doMenu()
    if choice == "a":
        doAdd()
    if choice == "v":
        doView()
#finish
print("Goodbye")