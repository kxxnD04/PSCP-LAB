"""Parity"""
def parity(txt, option):
    """binary"""
    check1 = 0
    if option == "Even":
        for i in txt:
            if i == "1":
                check1 += 1
        if check1%2 == 0:
            print(txt+"0")
        else:
            print(txt+"1")
    elif option == "Odd":
        for i in txt:
            if i == "1":
                check1 += 1
        if check1%2 == 0:
            print(txt+"1")
        else:
            print(txt+"0")
parity(input(), input())
