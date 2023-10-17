"""GCD_v1"""
def gcd(num1, num2):
    """find gcd of two value"""
    list1 = []
    num_process = max(num1, num2)
    for i in range(1, num_process+1):
        if num1%i == 0 and num2%i == 0:
            list1.append(i)
    print(max(list1))
gcd(int(input()), int(input()))
