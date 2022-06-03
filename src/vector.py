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
