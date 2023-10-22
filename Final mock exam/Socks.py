"""Socks"""
def socks(txt):
    """socks"""
    new = list(set(txt))
    ans = []
    for item in new:
        count = txt.count(item)
        ans.extend([str(item+item) for _ in range(count//2)])
    if ans:
        print(*sorted(ans))
    else:
        print('None')
    print(len(ans))


socks(input())
