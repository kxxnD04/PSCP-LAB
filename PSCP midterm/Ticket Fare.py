"""Ticket Fare"""
def ticket():
    """Dis"""
    nnn = int(input())
    aaa = int(input())
    bbb = int(input())
    ccc = int(input())
    ddd = int(input())
    eee = int(input())
    fff = int(input())
    ggg = int(input())
    if fff > nnn or ggg > nnn:
        print("Error")
    else:
        if ggg < fff:
            fff, ggg = ggg, fff
        if ggg <= fff+aaa:
            print(bbb)
        elif ggg <= fff+aaa+ccc:
            print(bbb+((ggg-(fff+aaa))*ddd))
        elif ggg > fff+aaa+ccc:
            print(bbb+(ccc*ddd)+((ggg-(fff+aaa+ccc))*eee))
ticket()
