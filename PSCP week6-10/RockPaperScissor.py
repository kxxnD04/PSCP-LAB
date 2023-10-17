"""RockPaperScissor"""
def rps(text):
    """play RockPaperScissor between A and B then find who should win """
    total_a = 0
    total_b = 0
    for i in range(0, len(text), 2):
        if text[i] == "P" and text[i+1] == "R":
            total_a += 1
        elif text[i] == "R" and text[i+1] == "P":
            total_b += 1
        elif text[i] == "P" and text[i+1] == "S":
            total_b += 1
        elif text[i] == "S" and text[i+1] == "P":
            total_a += 1
        elif text[i] == "S" and text[i+1] == "R":
            total_b += 1
        elif text[i] == "R" and text[i+1] == "S":
            total_a += 1
    if total_a > total_b:
        print("A win %d-%d" % (total_a, total_b))
    elif total_b > total_a:
        print("B win %d-%d" % (total_b, total_a))
    else:
        print("DRAW %d" % total_a)
rps(input())
