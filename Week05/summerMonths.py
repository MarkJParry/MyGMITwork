#Filename:  summerMonths.py
#Author:    Mark Parry
#Created:   19/02/2021
#Purpose:   Creates a tuple to store the months of the year and a second tuple to store the summer months.
#           I have added at third tuple to hold the seasons
#           Spring is 01-03,Summer is 04-07,Autumn is 08-10,Winter is 11-00) in terms of indices.

monthsInYear = ("January","February","March","April","May","June","July","August","September","October","November","December")
seasonsInYear = ("Spring","Summer","Autumn","Winter")

summerMonths = monthsInYear[5:8]
print(summerMonths)


