"""FOR!F-Ball"""
def ballswap(text):
    """find the last position of the swap when swap with way A, B and C"""
    last_pos = 1
    for i in text:
        if i == "A":
            if last_pos == 1:
                last_pos = 2
            elif last_pos == 2:
                last_pos = 1
        elif i == "B":
            if last_pos == 2:
                last_pos = 3
            elif last_pos == 3:
                last_pos = 2
        elif i == "C":
            if last_pos == 1:
                last_pos = 3
            elif last_pos == 3:
                last_pos = 1
    print(last_pos)
ballswap(input())
