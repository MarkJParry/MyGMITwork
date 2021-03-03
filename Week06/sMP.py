#Filename:  studentManagement.py
#Author:    Mark Parry
#Created:   25/02/2021
#Purpose:   Program to add and view students.
# 
# 
#set up dict

studentDetails = {  "Student1":{
                                "Name":"Mary",
                                "Courses":{
                                            "English":"A+",
                                            "Irish":"C-"
                                         },
                             },
                    "Student2":{
                                "Name":"Marky",
                                "Courses":{
                                            "English":"A",
                                            "Irish":"C+",
                                            "Physics":"B+"
                                         },
                              }
                 }



print("1. " , studentDetails.items())
print("1. " , studentDetails.keys())
print("1. " , studentDetails.values())
print("\n2. " , studentDetails["Student1"].items())
print("2. " , studentDetails["Student1"].keys())
print("2. " , studentDetails["Student1"].values())
print("2. " , studentDetails["Student1"]["Name"])

print("\n3. " , studentDetails["Student1"]["Courses"].items())
print("3. " , studentDetails["Student1"]["Courses"].keys())
print("3. " , studentDetails["Student1"]["Courses"].values())
print("3. " , studentDetails["Student1"]["Courses"][1]])
#print(studentDetails["Student1"]["Courses"]["English"])

input("Press return to continue")

for student, info in studentDetails.items():
    print("loop1 " + student + ':', studentDetails[student])
    for name, courses in info.items():
        print("loop2 " + name + ':', info[name])
        
        for course in courses:
            print("loop3 " + course + ':')
           # print(course + ':', courses[course])
#   for course in name.item():
#            print(course)

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