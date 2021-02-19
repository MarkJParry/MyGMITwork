#Filename:  studentDict.py
#Author:    Mark Parry
#Created:   19/02/2021
#Purpose:   Program that stores a student name and a list of their courses and grades in a dict and prints out their data.
#Note:      The number of courses a student has could change. Revisist this - are dicts immutable?
#References: https://www.w3schools.com/python/python_dictionaries_nested.asp  Nested Dictionaries

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
print(studentDetails)