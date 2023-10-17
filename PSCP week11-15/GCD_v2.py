"""GCDV2"""
def gcd_v2(num1, num2):
    """gcd_V2"""
    while num1 != 0:
        if num1 < num2:
            num1, num2 = num2, num1
        if num2 == 0:
            break
        num1, num2 = num1%num2, num2
    print(num2 if num2 != 0 else num1)
gcd_v2(int(input()), int(input()))
