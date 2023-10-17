""""MissingCard"""
def findmissingcard():
    """MissingCard"""
    group1 = set()
    for i in ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']:
        for j in ['S', 'H', 'D', 'C']:
            group1.add(i+j)
    for _ in range(51):
        group1.remove(input())
    print(*group1)
findmissingcard()
