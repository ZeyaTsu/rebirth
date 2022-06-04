import random
import math

#### Infinity Loop (Checker Loop)

def loopinf(value, function):
    for o in range(1, value):
        for p in range(1, value):
            function()
        value = value * 5
            
### Different of the while loop!
### value 4 = True
### value 0 = False
## Example
# rebirth.loopinf(4, hi)
# will repeat the hi() function infinity as long you don't change value by 0
# rebirth.loopinf(0, hi)
# the loop on the hi() function will end.
