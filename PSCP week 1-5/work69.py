"""Sequence VIII"""
def seq8(num):
    """68"""
    start = 2
    stop = 2
    num_space = num*3 -3
    for i in range(1, num+1):  #ลูปบน
        print(" "*num_space+"01", end=' ')
        for i in range(start, stop):
            print("%02d" % i, end=" ")
        stop += 1
        num_space -= 3
        print()
seq8(int(input()))
