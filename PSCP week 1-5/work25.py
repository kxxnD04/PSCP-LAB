"""25"""
def main1(aaa):
    """25"""
    return 2*aaa

def main2(aaa):
    """25"""
    return 3*(aaa**4)-(aaa**3)+(2*(aaa**2))+10

def main3(aaa, bbb, ccc):
    """25"""
    return ((aaa+ccc)**2)-(aaa*bbb)+(bbb**2)

def main4(aaa, bbb, ccc, ddd):
    """25"""
    return ((aaa**2)+(bbb**2)-(ccc**2))/((ddd**2)-(2*aaa*ddd)+(2*aaa))

def main():
    """25"""
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    ddd = float(input())
    print(main1(main1(aaa)))
    print(main2(main1(aaa-bbb)))
    print(main3(main1(aaa+bbb), main1(aaa+ccc), main2(main1(ddd**2))))
    print(main4((main3(main1(aaa+bbb), main1(aaa-ccc), main2(main1(ddd**2)))), \
main2(main1(aaa-bbb)), main1(main1(main1(main1(main1(ccc))))), ddd**8))
main()
