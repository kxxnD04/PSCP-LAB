"""Milk v2"""
def milk(lis1):
    """milk ที่แปลว่า นม"""
    get = lid = empty = lis1[5]//lis1[0]
    while True:
        if lid < lis1[1] and empty < lis1[3]:
            break
        if lid >= lis1[1]:
            get += lis1[2]
            lid += lis1[2]
            lid -= lis1[1]
            empty += lis1[2]
        if empty >= lis1[3]:
            get += lis1[4]
            empty += lis1[4]
            empty -= lis1[3]
            lid += lis1[4]
    print(int(get))
milk([float(input()), int(input()), int(input()), int(input()), int(input()), float(input())])
