"""Restaurant"""
def restaurant(aaa, bbb, ccc, ddd):
    """Is it worth it?"""
    if aaa < bbb:
        if ccc == 0:
            print("Yes")
        elif ddd == 0:
            print("Yes")
        else:
            total1 = (aaa + ddd)*((100-ccc)/100)
            if total1 > aaa:
                print("No %.3f" % (total1-aaa))
            elif total1 < aaa:
                print("Yes %.3f" % (aaa-total1))
            elif total1 == aaa:
                print("Yes")
    elif aaa == bbb:
        total1 = (aaa + ddd)*((100-ccc)/100)
        total2 = (aaa)*((100-ccc)/100)
        if total1 > total2:
            print("No %.3f" % (total1-total2))
        elif total1 < total2:
            print("Yes %.3f" % (total2-total1))
        elif total1 == total2:
            print("Yes")

restaurant(float(input()), float(input()), float(input()), float(input()))
