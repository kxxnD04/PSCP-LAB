"""Calculator"""
def calculator(num):
    """count how many press"""
    count = 0
    check = 0
    if num == 1:
        print(1)
    else:
        for i in range(1, num+1):
            txt = str(i)
            for _ in txt:
                check += 1
            count += (check+1)
            check = 0
        print(count)
calculator(int(input()))
