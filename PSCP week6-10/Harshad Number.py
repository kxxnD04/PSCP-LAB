"""Harshad Number"""
def harshadcheck():
    """check harshadcheck"""
    for _ in range(10):
        check = 0
        num = int(input())
        num = abs(num)
        for i in range(0, len(str(num))):
            check += int(str(num)[i])
        if  num == 0:
            print("No")
        elif num%check == 0:
            print("Yes")
        else:
            print("No")
harshadcheck()
