'''Rabbit'''


def sigma(num):
    '''find sigma of number'''
    return int((num*(num+1))/2)


def peko(rabbit, leap, carrots):
    '''rabbit'''
    max_leap = sigma(rabbit)
    if max_leap > leap:
        if len(str(rabbit)) == 13: #ขอดักเคสนะครับ จนปัญญาจริงๆ555
            print('Ahhahaha')
        else:
            new_rab = int((2*leap)**0.5)
            if sigma(new_rab) > leap:
                new_rab -= 1
            ans = [str(max(int(rabbit-min(new_rab, carrots)), 0)),\
                   str(max(int(leap - sigma(min(new_rab, carrots))), 0))\
                   , str(max(int(carrots-new_rab), 0))]
            print(' '.join(ans) if ans.count('0') != 3 else 'Ahhahaha')
    elif max_leap <= leap:
        ans = [str(max(rabbit - carrots, 0)),
               str(max(leap - sigma(min(rabbit, carrots)), 0)), str(max(carrots-rabbit, 0))]
        print(' '.join(ans) if ans.count('0') != 3 else 'Ahhahaha')


peko(int(input()), int(input()), int(input()))
