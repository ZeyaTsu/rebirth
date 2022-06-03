import random
import math

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
