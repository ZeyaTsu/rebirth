import random
import math

#### Number guesser
## Need rebirth.rand(min1, max1) (see example)

def guess(rand):
    guess = float(input("Rebirth| Guess > "))
    if guess == rand:
        print("Rebirth| You found the correct number.")
    elif guess < rand:
        print("Rebirth| Higher!")
    elif guess > rand:
        print("Rebirh| Lower!")
    return guess

# Example
# d = rebirth.rand(1, 10)
# s = True
# while s:
#    e = rebirth.guess(d)
#    if e == d:
#       s = False
#/!\ rebirth.rand(min1, max1) to make it work!
