#Filename:  counties.py
#Author:    Mark Parry
#Created:   12/03/2021
#Purpose:   Demonstrate Pie Chart usin matplotlib

import  matplotlib.pyplot as mpl 
import numpy as np


counties =["Clare","Galway","Limerick","Cork","Kerry"]
rCounties=[]

for county in range(0,100):
    #get a random number between 0 and 4 and use it to pick from counties to populate long list of counties(rCounites)
    rCounties.append(counties[np.random.randint(0,5)])

#count the occurences 
unique, counts = np.unique(rCounties,return_counts=True)

#find the position of the highest occurence - this returns an array and the type as there might be one or more of the same high value
result = np.where(counts == np.amax(counts))

#convert this to an integer for next step (make it explode on pie chart)
posMax = int(result[0][0])

#should populate this programatically rather than hard code here in case more or less unique values than the five counties
#but for this program its ok as we are only using five counties
explode = [0,0,0,0,0] #0 means no and 0.1 means yes
#replace the explode value with 0.1 to make the higest value stand out i.e. explode
explode[posMax] = 0.1

mpl.pie(counts,labels=unique,explode=explode,shadow=True)
mpl.show()
mpl.bar(unique, counts)
mpl.show()