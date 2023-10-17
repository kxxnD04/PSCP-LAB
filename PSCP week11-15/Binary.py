"""Bi_nary"""
def bi_narytwist(num):
    """base 10 nummber to base 2 number"""
    ans = ""
    while num != 0:
        ans += str(num%2)
        num //= 2
    print(int(ans[::-1]) if len(ans) > 0 else 0)

bi_narytwist(abs(int(input())))
