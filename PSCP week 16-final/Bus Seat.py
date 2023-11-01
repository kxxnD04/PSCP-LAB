'''Bus Seat'''
def busseat(each, seat, xxx, each2=0):
    """ต้องนั่งรถอะไร ถึงจะเข้าไปในใจเธอได้อะ"""
    for row in range(int(each+((each/2)-1))):
        if (row+1)%3 == 0:
            print()
        else:
            for col in range(seat):
                if (int((each-each2)+(each*(col)))) == xxx:
                    print('XX', end=' ')
                else:
                    print('%02d' % (int((each-each2)+(each*(col)))), end=' ')
            print()
            each2 += 1
busseat(int(input()), int(input()), int(input()))
