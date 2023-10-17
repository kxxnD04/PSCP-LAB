"""Triangle1"""
def tri1(side1, side2, side3):
    """47"""
    if side1 > side2:
        side1, side2 = side2, side1
    if side1 > side3:
        side1, side3 = side3, side1
    if side2 > side3:
        side2, side3 = side3, side2
    check1 = side3**2
    check2 = (side1**2) + (side2**2)
    if abs(check1-check2) > 0.01:
        print("No")
    else:
        print("Yes")
tri1(float(input()), float(input()), float(input()))
