"""Niwarn World"""
import math
def findx(nnn):
    """find x value"""
    return 2+((math.log2(nnn**2))/(2*nnn*math.log2(nnn)))
def findy(nnn, sss):
    """find y value"""
    return (math.sin(math.radians(30))+math.sqrt(2*sss))/(findx(nnn)+3)
def findz(kkk):
    """find z value"""
    return ((findy(kkk, kkk))**2)+((8456*(findx(kkk)**4))/(24*kkk))
def pfew(nnn, sss, kkk):
    """main"""
    print("X: %.1f, Y: %.1f, Z: %.1f" % (findx(nnn), findy(nnn, sss), findz(kkk)))
pfew(float(input()), float(input()), float(input()))
