"""Volleyball"""
def volleyball(txt):
    """play volleyball"""
    pointa = 0
    pointb = 0
    sets = 1
    awin = 0
    bwin = 0
    dew_check = 0
    for i in txt:
        pointa += 1*(1 if i == "A" else 0)
        pointb += 1*(1 if i == "B" else 0)
        if pointa == 24 and pointb == 24 and sets != 5:    #เช็คกรณีดิวของเซท 1-4
            dew_check = 1
        if (pointb == 25 or pointa == 25) and dew_check == 0 and sets != 5:  #นับแต้มเซท 1-4
            print("Set %d: A (%d) | B (%d)" % (sets, pointa, pointb))
            awin += 1*(1 if pointa > pointb else 0)
            bwin += 1*(1 if pointb > pointa else 0)
            pointb, pointa, sets = 0, 0, sets+1
        if dew_check == 1 and abs(pointa - pointb) == 2 and sets != 5:#จบเกมเมื่อเกิดการดิวเซท1-4
            print("Set %d: A (%d) | B (%d)" % (sets, pointa, pointb))
            awin += 1*(1 if pointa > pointb else 0)
            bwin += 1*(1 if pointb > pointa else 0)
            pointb, pointa, sets, dew_check = 0, 0, sets+1, 0
        if pointa == 14 and pointb == 14 and sets == 5:   #เช็คกรณีดิวของเซท 5
            dew_check = 1
        if (pointb == 15 or pointa == 15) and dew_check == 0 and sets == 5:   #นับแต้มเซท 5
            print("Set %d: A (%d) | B (%d)" % (sets, pointa, pointb))
            awin += 1*(1 if pointa > pointb else 0)
            bwin += 1*(1 if pointb > pointa else 0)
            pointb, pointa, sets = 0, 0, sets+1
        if dew_check == 1 and abs(pointa - pointb) == 2 and sets == 5:#กรณีจบเกมเมื่อเกิดการดิวเซท 5
            print("Set %d: A (%d) | B (%d)" % (sets, pointa, pointb))
            awin += 1*(1 if pointa > pointb else 0)
            bwin += 1*(1 if pointb > pointa else 0)
            pointb, pointa, sets, dew_check = 0, 0, sets+1, 0
        if awin == 3 or bwin == 3:
            break
    if sets != 6 and awin != 3 and bwin != 3:      #กรณียังหาผู้แพ้ชนะไม่ได้ และเกมยังไม่จบ
        print("Set %d: A (%d) | B (%d)" % (sets, pointa, pointb))
    if awin == 3:
        print("A won %d:%d set" % (awin, bwin))
    elif bwin == 3:
        print("B won %d:%d set" % (bwin, awin))
    else:
        print("The game has not finished yet.")
volleyball(input())
