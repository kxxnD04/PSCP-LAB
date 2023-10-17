"""COprime1"""
def coprime(num1, num2):
    """Check if two number is coprime"""
    list1 = []
    num_process = max(num1, num2)
    for i in range(1, num_process+1):
        if num1%i == 0 and num2%i == 0:
            list1.append(i)
    print("YES" if max(list1) == 1 else "NO")
    print(max(list1))
coprime(int(input()), int(input()))
