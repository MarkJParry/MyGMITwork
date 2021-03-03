#https://www.askpython.com/python/dictionary/python-dictionary-dict-tutorial

#set up dictionary for testing
students = {1: {'John':{'English':'A','Irish':'B'}},      
            2: {'John':{'English':'B','Irish':'B','Chemistry':'B+'}},
            3: {'Mark':{'English':'B','Irish':'D','Maths':'C'}},
            4: {'Mary':{'English':'A','Irish':'D','Maths':'A'}},
            5: {'John':{'Irish':'B'}}
         }

#print levels of the nested dictionaries and assign values to another dictionary
for student in students:
    print(student,students[student])
    names = students[student]
    for name in names:
        print(name,names[name])
        courses = names[name]
        for course in courses:
            print(course,courses[course])

#print level keys without values 
for student in students:
    print(student)
    names = students[student]
    for name in names:
        print(name)
        courses = names[name]
        for course in courses:
            print(course,courses[course])

#print levels with direct referencing (not reassigning values to another dictionary)
for student in students:
    print(student)
    for name in students[student]:
        print(name)
        for course in students[student][name]:
            print(course,students[student][name][course])

#loop through dictionary and return student ID keys if duplicate names - 
#zero length means not found, length 1 indicates exact match and length > 1 means duplicates found
#this can be checked by the calling statement upon return
def studentGetIds(studentName):
    studentIds = []
    for student in students:
        for name in students[student]:
            if studentName == name:
                studentIds.append(student)
    studentsFound = len(studentIds)
    return studentIds, studentsFound

#test the function
print(studentGetIds("John"))

def studentCourses(studentId,studentName):
    print("<---Student Details--->")
    print("Name: {}\tID: {}\n".format(studentName, studentId))
    print("Course   \tGrade")
    print("======   \t=====")
    for course in students[studentId][studentName]:
        print("{}    \t{}".format(course,students[studentId][studentName][course]))

#test the function
studentCourses(3, "Mark")

def checkMatches(studentsFound):
    if studentsFound == 0:
        match = "Not Found"
    elif studentsFound == 1:
        match = "Match"
    else: 
        match = "Duplicates" 
    return match

#test the function
print(checkMatches(1))
