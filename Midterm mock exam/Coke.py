"""Coke"""
def coke(aaa, bbb, ccc, ddd):
    """coke"""
    total = 0
    if not bbb:
        total += aaa*ddd
    elif ddd:
        if ddd%bbb:
            total += ((aaa*(ddd-(ddd//bbb)))+(ccc*(ddd//bbb)))
        else:
            total += ((aaa*(ddd-((ddd//bbb)-1)))+(ccc*((ddd//bbb)-1)))
    print(total)
coke(int(input()), int(input()), int(input()), int(input()))
