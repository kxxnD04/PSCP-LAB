"""Kayak""" #VERดีสุดละ
def main6(nnn, bbb):
    """KAYAK3ดาว"""
    total1, total2, group1 = [], [], [int(i) for i in bbb]
    group1.sort()
    while len(group1) != 2:
        get1, get2 = 0, 1
        while get2 != len(group1):
            num1 = abs(group1[get1]-group1[get2])
            total2.append(num1)
            get1 += 1
            get2 += 1
        ccc = min(total2)
        total1.append(ccc)
        get1, get2 = 0, 1
        while get2 != len(group1):
            num1 = abs(group1[get1]-group1[get2])
            if num1 == ccc:
                del group1[get1:get1+2]
                break
            get1 += 1
            get2 += 1
        total2 = []
    print(0 if nnn < 2 else sum(total1))
main6(int(input()), input().split())
