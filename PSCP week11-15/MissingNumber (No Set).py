"""MissingNumber (No Set)"""
def missingnumber(num):
    """Try Hard"""
    group1 = [i for i in range(1, num+1)]
    group2 = []
    while True:
        value = int(input())
        if value == 0:
            break
        group2.append(value)
    for i in group2:
        if i in group1:
            group1.remove(i)
    print(*group1, sep="\n")
missingnumber(int(input()))
