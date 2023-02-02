
def magicfunc(n, S): #n is an approximation of sqrt(S)
    return (n + S/n)/2

import math

guess = 1.5
print("Guess: ", guess)
print("Exact: ", math.sqrt(2))
print("----------------------")

for i in range(0,10):
    guess = magicfunc(guess, 2)
    print(guess)