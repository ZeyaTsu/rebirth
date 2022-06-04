import random
import math

#### For... loop

def loop(value, times, function):
    for value in range(1, times+1):
        function()

## Value is a 'group' it means that if you want to make a different loop you change the value (which is a
# number)
### Example
# rebirth.loop(1, 10, hi)
# it will repeat the hi() function 10 times in group1.
# rebirth.loop(2, 10, bye)
# it will repeat the bye() function 10 times in group2
