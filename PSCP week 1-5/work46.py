"""WeightStation"""
def weightcal(avgpoint, point1, point2, point3):
    """46"""
    point4 = avgpoint*4 - (point1+point2+point3)
    totalweight = point1 + point2 + point3 +point4
    balancecheck = avgpoint/2
    check1 = 0
    check2 = 0
    if totalweight > 15000:
        check1 += 1
    if abs(avgpoint-point1) > balancecheck:
        check2 += 1
    if abs(avgpoint-point2) > balancecheck:
        check2 += 1
    if abs(avgpoint-point3) > balancecheck:
        check2 += 1
    if abs(avgpoint-point4) > balancecheck:
        check2 += 1
    if check1 == 0 and check2 == 0:
        print("Pass %.2f" % point4)
    elif check1 == 1 and check2 == 0:
        print("Overweight")
    elif check1 == 1 and check2 > 0:
        print("Overweight")
    elif check1 == 0 and check2 > 0:
        print("Unbalance")
weightcal(float(input()), float(input()), float(input()), float(input()))
