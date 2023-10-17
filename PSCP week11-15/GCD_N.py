"""GCD_N"""
def find_gcd(num1, num2):
    """I dont even understand recursion TT"""
    if num1 < num2:
        num1, num2 = num2, num1
    if num2 != 0:
        return find_gcd(num1%num2, num2)
    else:
        return num1
def gcd_n(list1):
    """find gcd of N numbers"""
    for _ in range(len(list1)-1):
        list1 = list1[2:] + [find_gcd(*list1[0:2])]
    print(*list1)
gcd_n([int(input()) for _ in range(0, int(input()))])
