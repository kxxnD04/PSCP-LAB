"""All_Primes"""
def primes(num):
    """find all primes number from 1 to num"""
    check1 = 0
    check = 0
    for i in range(1, num+1):
        if i == 1:
            check1 += 0
        else:
            for j in range(1, (i//2)+1):
                if i%j == 0:
                    check += 1
            if check == 1:
                check1 += 1
            check = 0
    print(check1)
primes(int(input()))
