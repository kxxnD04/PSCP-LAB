"""Brick Bridge"""
def bridge(smalla, largeb, goal):
    """50"""
    if largeb*5 + smalla < goal:
        print(-1)
    elif largeb*5 + smalla == goal:
        print(smalla)
    else:
        if goal%5 == 0:
            if goal-(largeb*5) < 0:
                print(0)
            else:
                print(goal-(largeb*5))
        elif goal%5 != 0:
            newlargb = (goal-(goal%5))/5
            newsmalla = int(goal-(newlargb*5))
            if newlargb > largeb:
                newlargb = largeb
            if newsmalla > smalla:
                print(-1)
            else:
                print(int(goal-(newlargb*5)))
bridge(int(input()), int(input()), int(input()))
