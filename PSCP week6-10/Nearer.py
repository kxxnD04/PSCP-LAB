"""Nearer"""
def findnearer(alice, bob, icecream):
    """find nearest distance"""
    distance1 = abs(icecream-alice)
    distance2 = abs(icecream-bob)
    if distance1 > distance2:
        print("Bob %d" % distance2)
    elif distance2 > distance1:
        print("Alice %d" % distance1)
    else:
        print("Sundaes %d" % distance1)
findnearer(int(input()), int(input()), int(input()))
