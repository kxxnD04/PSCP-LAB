"""Sequence Xii"""
def seq12(num):
    """shape of square"""
    lenght_shape = (num-1)*-1
    for rows in range(lenght_shape, num):
        for collum in range(lenght_shape, num):
            print("%02d" % (num-abs(abs(rows)-abs(collum))), end=' ')
        print()
seq12(int(input()))
