#Filename:  popList.py
#Author:    Mark Parry
#Created:   19/02/2021
#Purpose:   Program that puts 10 random numbers into a queue(list), 
#           outputs all the values in the queue, 
#           removes the numbers from the queue one at a time, 
#           prints the removed and the rest of the queue. 
#           hint from AB (the command pop(0) takes the first element out of a list)

#import the random module in order to generate random numbers
import random

#initialise the queue
queue = []

#loop to populate the queue with 10 random numbers between 0 and 9
for x in range(0,10):
    queue.append(random.randrange(10))

#print the populated queue
print("The populated queue is: ", queue)

#loop through the queue , store the first element, remove it, print the rest of the queue
for x in range(0,10):
    popped = queue[0]
    queue.pop(0)
    print("Have just removed ", popped, "and the numbers left in the queue are ", queue)
print("The queue is now empty")
    
 
    

   

