"""OTP"""
def otp():
    """check valid or invalid otp"""
    ans = []
    while True:
        num = input().strip()
        if num == '0':
            break
        check = [num.count(i) for i in set(num)]
        if len(num) == 4:
            ans.append(('Valid') if check.count(2) == 1 else 'Invalid')
        elif len(num) == 6:
            ans.append(('Valid') if check.count(2) == 2 or check.count(3) == 1 else 'Invalid')
        elif len(num) == 8:
            ans.append(('Valid') if check.count(2) == 3 or check.count(3) == 2 else 'Invalid')
    print(*ans, sep='\n')
otp()
