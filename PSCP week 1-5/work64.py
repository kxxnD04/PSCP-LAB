"""Sequence III"""
def seq3(num):
    """63"""
    start = 2
    stop = num
    for i in range(1, num+1):
        for i in range(start, stop+2):
            print(i, end=' ')
        print(end="\n")
        start += 1
        stop += 1
seq3(int(input()))
