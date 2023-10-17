"""Semi Prime"""
def prime(num):
    """isPrime_large"""
    from math import floor
    check = True
    if num in range(0, 2):
        return False
    else:
        for i in range(2, floor(num**0.5)+1):
            if num%i == 0:
                check = False
                break
        return check
def semiprime(num):
    """primeeeeeeeee"""
    count_semi = 0
    for i in range(1, num+1):
        check = []
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                check.append(j)
                check.append(i//j)
                if prime(check[0]) == True and prime(check[1]) == True:
                    count_semi += 1
                    break
    print(count_semi)
semiprime(int(input()))
