"""Sequence VI"""
def seq6(num):
    """67"""
    start = 2
    stop = 2
    for i in range(1, num+1):
        print(1, end=' ')
        for i in range(start, stop):
            print(i, end=" ")
        stop += 1
        print()
seq6(int(input()))
