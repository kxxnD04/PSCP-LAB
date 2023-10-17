"""isprime_small"""
def isprime(num):
    """Check Prime number"""
    check = 0
    if num in range(0, 2):
        print("No")
    else:
        for i in range(1, (num//2)+1):
            if num%i == 0:
                check += 1
        print("Yes" if check == 1 else "No")
isprime(abs(int(input())))
