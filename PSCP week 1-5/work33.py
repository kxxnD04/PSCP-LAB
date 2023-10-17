'''Quadrant'''
def quadrant(pointx, pointy):
    '''33'''
    if pointx == 0 and pointy == 0:
        print("O")
    elif pointx > 0 and pointy > 0:
        print("Q1")
    elif pointx < 0 and pointy < 0:
        print("Q3")
    elif pointx > 0 and pointy < 0:
        print("Q4")
    elif pointx < 0 and pointy > 0:
        print("Q2")
    elif pointx == 0 and (pointy > 0 or pointy < 0):
        print("Y")
    elif (pointx > 0 or pointx < 0) and pointy == 0:
        print("X")
quadrant(int(input()), int(input()))
