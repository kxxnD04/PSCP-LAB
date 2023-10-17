"""Sequence VII"""
def seq7(num):
    """68"""
    start = 2
    stop = 2
    for i in range(1, num+1):  #ลูปบน
        print(1, end=' ')
        for i in range(start, stop):
            print(i, end=" ")
        stop += 1
        print()
    stop = num
    for i in range(1, num):   #ลูปล่าง
        print(1, end=' ')
        for i in range(start, stop):
            print(i, end=" ")
        stop -= 1
        print()
seq7(int(input()))
