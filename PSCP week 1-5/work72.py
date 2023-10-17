"""Sequence Xi""" # #ถ้าโค้ดนี้ไม่ถูกใจใครที่เข้ามาดู กราบขออภัย ครั้งหน้าจะเขียนให้ดีกว่าเดิม
def seq11half1(num): #ครึ่งบน
    """shape of square"""
    start = 1
    check2 = 1
    check3 = 1
    check4 = 3+(2*(num-3))
    check5 = 2
    for _ in range(0, 2*num-1):
        print("%02d" % start, end=' ')
    print()
    for i in range(0, num-2):
        check2 = 1
        for _ in range(check2, check3+1): #บันได
            print("%02d" % _, end=' ')
        for j in range(0, check4): #เติมเลขซ้ำ
            print("%02d" % check5, end=' ')
        for j in range(check5-1, 0, -1): #เติมเลขปิดท้าย
            print("%02d"% j, end=' ')
        check4 -= 2
        check3 += 1
        check5 += 1
        print()
    for i in range(1, num+1):
        print("%02d"% i, end=' ')
        if i == num:
            for i in range(num-1, 0, -1):
                print("%02d"% i, end=' ')
            break
    print()

def seq11half2(num): #ครึ่งล่าง
    """shape of square"""
    start = 1
    check2 = 1
    check3 = num-1
    check4 = 3
    check5 = num-1
    for _ in range(0, num-2):
        check2 = 1
        for _ in range(check2, check3): #บันไดเหมือนกันแค่เปลี่ยนลำดับนิดหน่อย
            print("%02d" % _, end=' ')
        for j in range(0, check4):  #เหมือนอันข้างบนแหละ
            print("%02d" % check5, end=' ')
        for j in range(check5-1, 0, -1): #ไม่ต่างกัน
            print("%02d"% j, end=' ')
        check4 += 2
        check3 -= 1
        check5 -= 1
        print()
    for _ in range(0, 2*num-1):
        print("%02d" % start, end=' ')
    print()

def seq11(num):
    """Shape of square"""
    if num == 1:
        print("01")
    else:
        seq11half1(num)
        seq11half2(num)
seq11(int(input()))
