#set up dictionary for testing
students = {1: {'John':{'English':'A','Irish':'B'}},      
            2: {'John':{'English':'B','Irish':'B','Chemistry':'B+'}},
            3: {'Mark':{'English':'B','Irish':'D','Maths':'C'}}
         }
def getNewStudentId():
    studentId = int(max(students) +1)
    return studentId

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
        
    #print(courses)
    names[studentName] = courses
    #print(names)
    students[studentId] = names
    print(students[studentId], " added to dictionary")
    return

studentAdd()
print(students)