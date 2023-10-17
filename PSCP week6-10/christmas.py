"""Chrismastree"""
def  christmas(nnn, kkk):
    """Week6"""
    check1 = nnn  #จำนวนช่องว่าง
    check2 = 1   #จำนวนดอกจัน
    for _ in range(1, nnn+1):
        print(" "*(check1-1), end="")
        print("*"*check2)
        check1 -= 1
        check2 += 2
    for _ in range(0, kkk):
        print(" "*(nnn-2), end="")
        print("---")
christmas(int(input()), int(input()))
