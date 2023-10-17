"""Ink"""
def ink(line1):
    """INK SPREADING"""
    from math import ceil
    for _ in range(line1[1]):
        point = [int(i) for i in input().split()]
        space_point = ((((point[0]**2) + (point[1]**2))**0.5)**2)*3.1416
        print(0 if point == [0, 0] else ceil(space_point/line1[0]))

ink([int(i) for i in input().split()])
