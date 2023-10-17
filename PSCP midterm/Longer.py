"""Longer"""
def longer(radius, a_long, b_long):
    """longer"""
    from math import pi
    line1 = "Circle is longer"*(2*pi*radius > 2*(a_long+b_long))\
    +"Rectangle is longer"*(2*pi*radius < 2*(a_long+b_long))+\
    "Equal"*(2*pi*radius == 2*(a_long+b_long))
    line2 = abs((2*pi*radius) - (2*(a_long+b_long)))
    print(line1)
    print("%.5f" % line2)
longer(float(input()), float(input()), float(input()))
