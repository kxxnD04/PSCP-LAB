"""Sequence I"""
def seq1(num):
    """62"""
    for i in range(1, num+1):
        for i in range(1, num+1):
            print(i, end=' ')
        print(end="\n")
seq1(int(input()))
