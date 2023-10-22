"""Water"""


def water(nnn, aaa, bbb, ccc, ddd):
    """water price"""
    ans = 0
    each = [float(input()) for _ in range(nnn)]
    for i in each:
        cal = aaa*(min(bbb, i))
        cal += max(i-bbb, 0)*ccc
        if cal <= ddd:
            cal = 0
        ans += cal
    print('%.2f' % ans)


water(int(input()), float(input()), float(input()), float(input()), float(input()))
