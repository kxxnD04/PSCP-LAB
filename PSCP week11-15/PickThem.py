"""PickThem"""
def pickthem(txt):
    """pickthem"""
    txt = ((txt.strip("[")).strip("]")).split(", ")
    check = 0
    for i in txt:
        if int(i)%2 == 0:
            print(i)
            check += 1
    if check == 0:
        print("Nope")
pickthem(input())
