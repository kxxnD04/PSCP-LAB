'''line sorting'''
def lines(vare):
    '''lines'''
    list1 = []
    for _ in range(vare):
        list1.append(input())
    list1.sort(key=len)
    print(*list1, sep="\n")
lines(int(input()))
