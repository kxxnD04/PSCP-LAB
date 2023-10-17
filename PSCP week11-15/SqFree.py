"""SqFree"""
def sqfree(num, ans=0):
    """Square free number?"""
    for i in range(1, num+1):
        check = True
        for j in range(1, int(i**0.5)+1):
            if i % (j**2) == 0 and j != 1:
                check = False
                break
        ans += 1 if check else 0
    print(ans)
sqfree(int(input()))
