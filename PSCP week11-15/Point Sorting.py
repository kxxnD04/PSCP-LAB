"""Point Sorting"""
def value(lis):
    """key to sort"""
    return int(lis[0])+int(lis[-1]), int(lis[0])
def pointso_rt(num):
    """main function"""
    group1 = []
    for _ in range(num):
        num2 = int(input())
        for _ in range(num2):
            group1.append(input().split())
        group1.sort(key=value)
        for i in group1:
            print(*i)
        group1 = []
pointso_rt(int(input()))
