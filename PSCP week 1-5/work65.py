"""Sequence IV"""
def seq4(num):
    """65"""
    start = 1
    stop = num
    for i in range(1, num+1):
        for i in range(start, stop+1):
            print(i, end=' ')
        print(end="\n")
        start += num
        stop += num
seq4(int(input()))
