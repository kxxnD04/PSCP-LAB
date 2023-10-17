"""Coke"""
def coke(aaa, bbb, ccc, ddd):
    """coke"""
    total = 0
    if bbb == 0 and ddd != 0:
        total += aaa*ddd
    elif bbb != 0 and ccc != 0 and ddd != 0:
        if ddd%bbb != 0:
            total += ((aaa*(ddd-(ddd//bbb)))+(ccc*(ddd//bbb)))
        elif ddd%bbb == 0:
            total += ((aaa*(ddd-((ddd//bbb)-1)))+(ccc*((ddd//bbb)-1)))
    elif bbb != 0 and ccc == 0 and ddd != 0:
        if ddd%bbb == 0:
            total += ((aaa*(ddd-((ddd//bbb)-1)))+(ccc*((ddd//bbb)-1)))
        elif ddd%bbb != 0:
            total += ((aaa*(ddd-((ddd//bbb))))+(ccc*((ddd//bbb))))
    elif ddd == 0:
        total = 0
    print(total)
coke(int(input()), int(input()), int(input()), int(input()))
