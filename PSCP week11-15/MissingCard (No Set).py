""""MissingCard (No Set)"""
def findmissingcard():
    """MissingCard (No Set)"""
    group1 = []
    for i in ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']:
        for j in ['S', 'H', 'D', 'C']:
            group1.append(i+j)
    for _ in range(51):
        group1.remove(input())
    print(*group1)
findmissingcard()
