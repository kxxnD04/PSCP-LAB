"""Sequence X""" #ถ้าโค้ดนี้ไม่ถูกใจใครที่เข้ามาดู กราบขออภัย ครั้งหน้าจะเขียนให้ดีกว่าเดิม
def seq10(num):
    """shape of Rhombus"""
    for i in range(1, num+1): #Credits Bboonz สามเหลี่ยมบน
        for _ in range(num-i):
            print("  ", end=' ')
        for j in range(i):
            print("%02d"% (j+1), end=' ')
        for j in range(i-1, 0, -1):
            print("%02d"% j, end=' ')
        print()
    for i in range(1, num):  #สามเหลี่ยมล่าง
        for _ in range(3*i):
            print(" ", end='')
        for j in range(1, num-i+1):
            print("%02d"% j, end=' ')
        for j in range(num-i-1, 0, -1):
            print("%02d"% j, end=' ')
        print()
seq10(int(input()))
