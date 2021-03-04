#Filename:  testDictrwJson.py
#Author:    Mark Parry
#Created:   04/03/2021
#Purpose:   uses the json module, reads from and write to a json format file

#use students dictionary from earlier programs
students = {1: {'John':{'English':'A','Irish':'B'}},      
            2: {'John':{'English':'B','Irish':'B','Chemistry':'B+'}},
            3: {'Mark':{'English':'B','Irish':'D','Maths':'C'}},
            4: {'Mary':{'English':'A','Irish':'D','Maths':'A'}},
            5: {'John':{'Irish':'B'}}
         }

import json
filename = "students.json"

def dumpDict():
   with open(filename) as outfile:
      json.dump(students, outfile)

def loadDict():
   with open(filename) as infile:
      return json.load(infile)
      
      
newDict = loadDict()
print(newDict)