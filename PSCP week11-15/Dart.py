"""Dart"""
def dart(list1, ans=0):
    """Playing Dart"""
    for i in list1:
        dis = ((i[0]**2) + (i[1]**2))**0.5
        if dis >= 0 and dis <= 2:
            ans += 5
        elif dis > 2 and dis <= 4:
            ans += 4
        elif dis > 4 and dis <= 6:
            ans += 3
        elif dis > 6 and dis <= 8:
            ans += 2
        elif dis > 8 and dis <= 10:
            ans += 1
    print(ans)
dart([[int(i) for i in input().split()] for _ in range(int(input()))])
