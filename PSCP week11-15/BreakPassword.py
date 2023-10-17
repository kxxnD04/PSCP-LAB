"""BreakPassword"""
import hashlib
def breakpass(txt):
    """brute force for password"""
    for i in range(0, 100000):
        num = "%05d" % i
        if hashlib.sha512(num.encode('utf-8')).hexdigest().upper() == txt:
            print(num)
            break

breakpass(input())
