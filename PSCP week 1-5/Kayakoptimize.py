"""kayak"""
def kayak(num, list1, ans=0):
    """optimize?"""
    for _ in range(num-1):
        mi_n = [abs(list1[i]-list1[i+1]) for i in range(len(list1)-1)]
        ans += min(mi_n)
        del list1[mi_n.index(min(mi_n)):mi_n.index(min(mi_n))+2]
    print(ans)
kayak(int(input()), sorted(list(map(int, input().split()))))
