"""Sequence IX""" #ถ้าโค้ดนี้ไม่ถูกใจใครที่เข้ามาดู กราบขออภัย ครั้งหน้าจะเขียนให้ดีกว่าเดิม
def seq6(num): #ลูปหลัง
    """67"""
    s_top = 0
    for i in range(num-1, s_top, -1):
        print("%02d" % i, end=" ")

def seq9(num):
    """68"""
    start = 2
    stop = 2
    num2 = 1
    num_space = num*3 -3
    for i in range(0, num):  #ลูปหน้า
        print(" "*num_space+"01", end=' ')
        for i in range(start, stop):
            print("%02d" % i, end=" ")
        seq6(num2)
        num2 += 1
        stop += 1
        num_space -= 3
        print()
seq9(int(input()))
