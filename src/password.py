import random
import math

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
