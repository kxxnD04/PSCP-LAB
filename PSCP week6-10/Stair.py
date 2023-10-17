"""Stair"""
def gotosecondfloor(heigh, num):
    """find least step"""
    total_countstep = 0
    checkno = 0
    heighcheck = 0
    while num != 0:
        stairheigh = int(input())
        num -= 1
        if heigh < stairheigh or checkno == 1:
            checkno = 1
            continue
        else:
            heighcheck += stairheigh
            if heighcheck == heigh:
                total_countstep += 1
                heighcheck = 0
            elif heighcheck > heigh:
                heighcheck = stairheigh
                total_countstep += 1
    if total_countstep == 0 and heighcheck > 0:
        total_countstep += 1
    elif total_countstep != 0 and heigh >= heighcheck > 0:
        total_countstep += 1
    print(total_countstep if checkno == 0 else "NO")

gotosecondfloor(int(input()), int(input()))
