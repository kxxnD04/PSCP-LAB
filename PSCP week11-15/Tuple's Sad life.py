"""Tuple's Sad life"""
def sadlife():
    """SO SAD <e>judge"""
    group1 = tuple(input().split())
    num = str(input())
    for _ in range(group1.count(num)):
        for _ in range(group1.count(num)):
            print(group1.index(num), end=" ")
        print()
sadlife()
