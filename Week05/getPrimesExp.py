#Filename:  getPrimesExp.py
#Author:    Mark Parry
#Created:   17/02/2021
#Purpose:   Determines if a number is a prime from a range of numbers from 2 to N  plying around with methods.
#Note:      A prime is a number divisible only by itself and one.
#References: Week 5 lecture on Primes Andrew Beatty
N = 100000
candidateList = []
primes = [2]



for candidate in range(3, N + 1,2):
    #candidateList.append(candidate)

#divide the number by the divisor

    isPrime = True 
    for divisor in primes:
      
        if candidate % divisor == 0:
            isPrime = False
            break
       
    if isPrime:
        primes.append(candidate)
           


print(primes)       