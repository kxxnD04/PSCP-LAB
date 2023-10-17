"""Ball"""
def ball(heigh):
    """find number of bounch of the ball when let it fall from a height"""
    heigh *= 100
    count = 0
    while heigh >= 1:
        heigh *= 0.6
        count += 1
    print(count-1)
ball(float(input()))
