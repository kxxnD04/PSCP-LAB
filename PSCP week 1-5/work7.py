"""D1"""
def main1(aaa):
    """wk1"""
    return aaa+1

def main2(aaa):
    """wk1"""
    return (7*(aaa**3))+(2*(aaa**2))-(31*aaa)+1

def main3(aaa):
    """wk1"""
    return (-1)*aaa

def main4(aaa, bbb):
    """wk1"""
    return (aaa-bbb)*(aaa+bbb)

def main5(aaa, bbb, ccc):
    """wk1"""
    return (bbb-(((bbb**2)-(4*aaa*ccc))**0.5))/(2*aaa)

def main6():
    """HAHA"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    print(main1(num1))
    print(main2(num2))
    print(main3(num3))
    print(main4(num1, num2))
    print(main5(num1, num2, num3))
main6()
