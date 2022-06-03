import random
import math

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
