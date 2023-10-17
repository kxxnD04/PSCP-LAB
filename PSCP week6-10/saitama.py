"""Saitama"""
def sor_t(num1, num2, num3, num4):
    """sor_t number from highest to lowest"""
    if num1 < num2:
        num1, num2 = num2, num1
    if num1 < num3:
        num1, num3 = num3, num1
    if num1 < num4:
        num1, num4 = num4, num1
    return num1

def saitamaquest(quest1, quest2, quest3, quest4):
    """how many days to do saitama quest"""
    from math import ceil
    numq1, numq2 = int(input()), int(input())
    numq3, numq4 = int(input()), int(input())
    check1, check2 = ceil(quest1/numq1), ceil(quest2/numq2)
    check3, check4 = ceil(quest3/numq4), ceil(quest4/numq3)
    print(sor_t(check1, check2, check3, check4))
saitamaquest(int(input()), int(input()), int(input()), int(input()))
