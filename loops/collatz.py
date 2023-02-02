import math

def collatz(n):
    if((n % 2) == 0):
        n = n//2
    else:
        n = 3*n+1
    return n

mynum = int(input("Please type a positive integer: "))

print(mynum)
while(mynum > 1):
    mynum = collatz(mynum)
    print(mynum)
