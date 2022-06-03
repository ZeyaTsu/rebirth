import random
import math
#### Vector: coordinates from points xA, yA, xB, Yb | DET

def vector_x(xa, xb):
    Pa = xb - xa
    return Pa 

def vector_y(ya, yb):
    Pb = yb - ya
    return Pb

def vector_det(x, y, x1, y1):
    det = (x * y1) - (y * x1)
    return det

# Example
# a = vector_x(6, 12)
# b = vector_y(12, 6)
# print(a,b)
# = 6 -6
# c = vector_det(a, b, a1, b1)
# print(c)

#### Generate a random number

def rand(min1, max1):
    rand = random.randint(min1, max1)
    return rand

# d = rebirth.rand(1, 10)
# print(d) random number.
    
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

# Number generator from Pi

def pi_gen(value, times):
    pi_gen = math.pi
    for i in range(1, times+1):
        pi_gen += value
        print(pi_gen)

# Example
# rebirth.pi_gen(2.124, 5)
# = 5.265592653589794
#   7.389592653589794
#   9.513592653589795
#   11.637592653589795
#   13.761592653589796

#### All informations about the Python Module

def info():
    print("Rebirth | Python Module")
    print("- A simple python module using simple functions")
    print("- Useful for some things like vector calculations")
    print("- Less useful but still good like pi_gen")
    print("- Made for fun.")
    return info

# rebirth.info()

#### Generating password /!\ Have fun to customize it by yourself

def password(len):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbol = "[]{}#()*;._-"
    ans = lower_case + upper_case + number + symbol

    length = len
    password = "".join(random.sample(ans, length))

    return password

#### Example
# print("Your new password is", rebirth.password(6))
## OR
# length = int(input("Password length: "))
# print("Your new password is", rebirth.password(length))

#### Ping
def ping():
    print("Pong(1)")
    return ping
    
#### Number: Odd or Even 

def odd_even(number, messageEven, messageOdd):
    if number % 2:
        print(messageOdd)
    else:
        print(messageEven)

# Example
# rebirth.odd_even(2, "Even", "Odd")
# = Even
## IF YOU WANT 0 MESSAGE TO SAY ODD OR EVEN
# rebirth.odd_even(2, "", "")
# = 
## OTHER EXAMPLE
# rebirth.odd_even(rebirth.rand(1,20), "Even", "Odd")
