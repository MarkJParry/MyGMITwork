#Filename:  studentManagement.py
#Author:    Mark Parry
#Created:   25/02/2021
#Purpose:   Program to add and view students.

#set up dictionary for testing
students = {1: {'John':{'English':'A','Irish':'B'}},      
            2: {'John':{'English':'B','Irish':'B','Chemistry':'B+'}},
            3: {'Mark':{'English':'B','Irish':'D','Maths':'C'}}
         }
#function to display menu
def studentMenu():
    option = input("\nPlease choose from the following options:\n[a] Add a New Student\n[v] View an Existing Student\n[q] Quit\nType the letter a, v or q ").strip()
    return option

#function to add a student to the dictionary
def studentAdd():
    print("In Add")
    aName = "InAdd"
    while (aName != ""):
        aName = input("Enter the name of the student you would like to add:\nLeave this blank to return to the menu ").strip()

#function to view a student in the dictionary
def studentView():
    s_id = studentSelect()
    if s_id !=0:
        #print("Student Id: ",s_id)
        studentPrint(s_id)
    else:
        print("\nStudent not found")
    return

#function to select  a student (if duplicate names in the dictionary presents choice of IDS)
def studentSelect():

    nameIn = input("Enter student name: ").strip()
    s_ids = studentGetIds(nameIn)

    if len(s_ids) == 0:
        s_id = 0
    elif len(s_ids) > 1:
        s_id = int(input("There are {} students called {} which one do you want to view {}: ".format(len(s_ids),nameIn,s_ids)))
    else:
        s_id = s_ids[0]
    return s_id

# function to return student IDS for any name or duplicate names
def studentGetIds(nameIn):
    s_ids = []
    for s_id, s_info in students.items():
        for name, c_info in s_info.items():
            if nameIn == name:
                s_ids.append(s_id)

    return s_ids


#function to display the selected students info
def studentPrint(s_id_in):
    for s_id, s_info in students.items():
        if s_id == s_id_in:
            print("\nStudent ID:", s_id)
        
            for name, c_info in s_info.items():
                print("Name:", name)
                print("Course     \tGrade")
            
                for course in c_info:
                    print("{}     \t{}".format(course, c_info[course]))
    return


#start - Main body of program
choice = ""
while (choice != "q"):
    choice = studentMenu()
    if choice == "a":
        studentAdd()
    if choice == "v":
        studentView()
#finish
print("Goodbye")



