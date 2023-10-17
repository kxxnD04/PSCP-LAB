"""MissingNumber"""
def missing2(num):
    """MissingNumber with Set"""
    set1 = set(range(1, num+1))
    set2 = set()
    while True:
        value = int(input())
        if value == 0:
            break
        set2.add(value)
    missing_set = sorted(set1.difference(set2))
    print(*missing_set, sep="\n")

missing2(int(input()))
