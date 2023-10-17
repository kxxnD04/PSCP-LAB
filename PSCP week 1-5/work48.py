"""SurprisingVote"""
def surprise(total, mostscore):
    """48"""
    if mostscore*2 <= total:
        restscore = total-(mostscore*2)
        if abs(mostscore - restscore) > 2:
            print("Surprising")
        else:
            print("Not surprising")
    else:
        restscore = 0
        if abs(mostscore - restscore) > 2:
            print("Surprising")
        else:
            print("Not surprising")
surprise(float(input()), float(input()))
