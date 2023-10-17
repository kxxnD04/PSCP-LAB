"""isPrime_large"""
def prime_large(num):
    """isPrime_large"""
    from math import floor
    check = "YES"
    if num in range(0, 2):
        print("NO")
    else:
        for i in range(2, floor(num**0.5)+1):
            if num%i == 0:
                check = 'NO'
                break
        print(check)
prime_large(int(input()))
