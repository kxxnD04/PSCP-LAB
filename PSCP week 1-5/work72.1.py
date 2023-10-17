"""Sequence Xi""" # ขอจัดระเบียบโค้ดก่อนเดี๋ยวมาส่งใหม่ฮะ
def seq11(num): 
    """shape of square"""
    lenght_shape = (num-1)*-1
    for rows in range(lenght_shape, num):
        for collum in range(lenght_shape, num):
            print("%02d" % (num-max(abs(rows), abs(collum))), end=' ')
        print()
seq11(int(input()))
