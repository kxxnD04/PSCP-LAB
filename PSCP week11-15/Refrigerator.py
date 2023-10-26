"""Refrigerator"""
def refrig(nnn, list1, ans=0):
    """Johny Walker in my Refrigerator"""
    while 0 not in list1 and nnn:
        keep = list1.pop(0)
        list1 = (list(map(lambda x: x-1, list1)))
        list1.append(keep)
        ans += 1
        list1.sort()
    print(ans)
refrig(int(input()), sorted([int(i) for i in input().split()]))
