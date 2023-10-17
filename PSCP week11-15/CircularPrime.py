"""CircularPrime"""
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
def cir_prime(num):
    """cir prime"""
    ans = 0
    for i in range(2, num+1):
        list1 = [i]
        cir = str(i)
        check = True
        for _ in range(len(str(i))-1):
            list1.append(int(cir[1:]+cir[0]))
            cir = str(cir[1:]+cir[0])
        for j in list1:
            if prime(j) == False:
                check = False
                break
        ans += i if check == True else 0
    print(ans)
cir_prime(int(input()))
