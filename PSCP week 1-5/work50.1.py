"""Largest Number"""
def main(num1, num2, num3):
    """50"""
    if int(num1+num2) < int(num2+num1):
        num1, num2 = num2, num1
    if int(num1+num3) < int(num3+num1):
        num1, num3 = num3, num1
    if int(num2+num3) < int(num3+num2):
        num2, num3 = num3, num2
    print(int(num1+num2+num3))
main(str(input()), str(input()), str(input()))
