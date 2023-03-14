"""
Takes two values and returns the first one raised to the power of the second.
"""

def exponentiate(i1,i2):
    return i1**i2


"""
Takes one value and raises it to the fourth power
"""

def raise_to_fourth_power(num : int):
    return exponentiate(num,4)
    
square = lambda val : exponentiate(val,2)
cube = lambda val : exponentiate(val,3)


print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))