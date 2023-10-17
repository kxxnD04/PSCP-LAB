"""isPrime_large(larger)"""
def prime_large(num):
    """isPrime_large(larger)"""
    check = "True"
    if num in range(0, 2):
        print("False")
    else:
        if num%2 == 0:
            if num == 2:
                check = 'True'
            else:
                check = 'False'
        else:
            for i in range(3, int(num**0.5)+1, 2):
                if num%i == 0:
                    check = 'False'
                    break
        print(check)
prime_large(int(input()))
