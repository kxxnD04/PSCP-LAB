"""PickThemAgain"""
def pickagain(txt):
    '''pick them again'''
    txt = txt.split(" ")
    check = 0
    for i in range(-1, -1*len(txt)-1, -1):
        if int(txt[i]) % 3 == 0 or int(txt[i]) % 5 == 0:
            print(txt[i])
            check += 1
    if check == 0:
        print("Nope")
pickagain(input())
