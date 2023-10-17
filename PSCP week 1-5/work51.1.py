"""Brick Bridge"""
def bridge(smalla, largeb, goal):
    """51"""
    needb = ((goal//5 > largeb) * largeb) + ((goal//5 <= largeb) * goal//5)
    needa = goal-needb*5
    print(-1 if needa > smalla else needa)
bridge(int(input()), int(input()), int(input()))
