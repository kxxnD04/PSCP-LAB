"""LeftArrow"""
def main(aaa, bbb):
    """Chillbro"""
    num1 = 0
    for num1 in range((bbb//2)+1):
        print(" "*((bbb//2)-num1) + "*"*aaa)
        num1 += 1
    num1 = 1
    for num1 in range((bbb//2)):
        print(" "*(num1+1)+"*"*aaa)
        num1 += 1
main(int(input()), int(input()))
