#Filename:  studentManagement.py
#Author:    Mark Parry
#Created:   25/02/2021
#Purpose:   Program to add and view students.

#set up dictionary for testing
students = {1: {'John':{'English':'A','Irish':'B'}},      
            2: {'John':{'English':'B','Irish':'B','Chemistry':'B+'}},
            3: {'Mark':{'English':'B','Irish':'D','Maths':'C'}},
            4: {'Mary':{'English':'A','Irish':'D','Maths':'A'}},
            5: {'John':{'Irish':'B'}}
         }
#function to display menu
def studentMenu():
    option = input("\nPlease choose from the following options:\n[a] Add a New Student\n[v] View an Existing Student\n[q] Quit\nType the letter a, v or q ").strip()
    return option


#function to add a student to the dictionary
def studentAdd():
    cname = 'Start'
    courses = {}
    names ={}
    
    studentName = input('Please enter student name: ').strip()

    if studentName == "":
        return

    studentId = getNewStudentId()

    while cname != "":
        cname = input("Course:").strip()
        if cname != "":
           cgrade = input("Grade:").strip()
           courses[cname] = cgrade
        
    #add courses dict to names dictionary
    names[studentName] = courses
    #add names dict to students dictionary
    students[studentId] = names
    print(students[studentId], " added to dictionary")
    return

#function to get the highest value of studentId in dictionary and increment it by 1 for a new student
def getNewStudentId():
    studentId = int(max(students) +1)
    return studentId

#function to view a student in the dictionary
def studentView():
    studentId,studentName = studentSelect()
    if studentId !=0:
        #print("Student Id: ",studentId)
        studentCourses(studentId,studentName)
    else:
        print("\nStudent not found")
    return

#function to select  a student (if duplicate names in the dictionary presents choice of IDS)
def studentSelect():

    studentName = input("Enter student name: ").strip()
    studentIds,studentsFound = studentGetIds(studentName)

    if studentsFound == 0:
        studentId = 0
    elif studentsFound > 1:
        studentId = int(input("There are {} students called {} which one do you want to view {}: ".format(len(studentIds),studentName,studentIds)))
    else:
        studentId = studentIds[0]
    return studentId, studentName

#function to return student IDS for any name or duplicate names
def studentGetIds(studentName):
    studentIds = []
    for student in students:
        for name in students[student]:
            if studentName == name:
                studentIds.append(student)
    studentsFound = len(studentIds)
    return studentIds, studentsFound


#function to display the selected students info
def studentCourses(studentId,studentName):
    print("<---Student Details--->")
    print("Name: {}\tID: {}\n".format(studentName, studentId))
    print("Course   \tGrade")
    print("======   \t=====")
    for course in students[studentId][studentName]:
        print("{}    \t{}".format(course,students[studentId][studentName][course]))

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



