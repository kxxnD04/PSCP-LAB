"""SMS"""
def sms(loop):
    """SMS"""
    list1 = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    ans = []
    for _ in range(loop):
        number, times = int(input()), int(input())
        if number == 1:
            for _ in range(times):
                if len(ans) > 0:
                    del ans[-1]
        elif number in range(2, 7):
            ans.append((list1[number-2])[times%3 -1])
        elif number == 8:
            ans.append((list1[number-2])[times%3 -1])
        else:
            ans.append((list1[number-2])[times%4 -1])
    if ans == []:
        print("null")
    else:
        print(*ans, sep='')

sms(int(input()))
