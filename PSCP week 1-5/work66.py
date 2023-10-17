"""Sequence V"""
def seq5(num):
    """66"""
    check7 = []
    for i in range(num, 0, -1):
        check7.append(i)
        print(i, end=' ')
        if len(check7) == 7:
            print(end="\n")
            check7.clear()
seq5(int(input()))
