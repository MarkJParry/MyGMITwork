#Filename:  studentDict.py
#Author:    Mark Parry
#Created:   19/02/2021
#Purpose:   Program that stores a student name and a list of their courses and grades in a dict and prints out their data.
#Note:      The number of courses a student has could change. Revisit this - are dicts immutable?
#References: https://www.w3schools.com/python/python_dictionaries_nested.asp  Nested Dictionaries

#set up dict
studentDetails = {  "Student1":{
                                "Name":"Mary",
                                "Courses":{
                                            "English":"A+",
                                            "Irish":"C-"
                                         },
                             },
                    "Student2":{
                                "Name":"Mark",
                                "Courses":{
                                            "English":"A",
                                            "Irish":"C+",
                                            "Physics":"B+"
                                         },
                              }
                 }
print(studentDetails)   
print(len(studentDetails))
for student, names in studentDetails.items():
    print(student)
    for name, courses  in names.items():
        print(name, courses)
    for course in courses:
        print(course, courses[course])

for student in studentDetails
   print(studentDetail[student])
   for detail,rest in details.items():
      # print(detail,rest)
     