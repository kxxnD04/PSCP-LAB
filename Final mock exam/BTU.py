"""BTU"""


def btu(size, heigh, people, heat, sun):
    """btu"""
    ans = 5000*(size in range(100, 151)) + 6000*(size in range(151, 251))\
+ 7000*(size in range(251, 301)) + 8000*(size in range(301, 351))\
+ 9000*(size in range(351, 401)) + 10000*(size in range(401, 451))\
+ 12000*(size in range(451, 551)) + 14000*(size in range(551, 701))\
+ 18000*(size in range(701, 1001))\
+ 21000*(size in range(1001, 1201)) + 23000*(size in range(1201, 1401))\
+ 24000*(size in range(1401, 1501))\
+ 30000*(size in range(1501, 2001)) + 34000*(size in range(2001, 2501))
    ans += (max(heigh-8, 0)*1000) + (max(people-2, 0)*600) +\
        (4000*(heat == 'kitchen'))
    if sun == 'facing the sun':
        ans = ans*(110/100)
    elif sun == 'shaded':
        ans = ans*(90/100)
    print(int(ans))


btu(int(input()), int(input()), int(input()), input(), input())
