"""Century"""
def findcentury(lap):
    """Find century"""
    from math import ceil
    num = ""
    for _ in range(lap):
        txt = input()
        for i in txt:
            if i.isnumeric():
                num += str(i)
        if txt[0:4] == "A.D.":
            print(ceil((int(num))*0.01))
        elif txt[0:4] == "B.E.":
            if int(num) < 544:
                print("ERROR")
            else:
                num = int(num) - 543
                print(ceil((int(num))*0.01))
        num = ""
findcentury(int(input()))
