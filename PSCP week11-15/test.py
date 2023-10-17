'''Rabbit'''
 
 
def peko(rabbit, leap, carrots):
    '''rabbit'''
    rab_ans = 0
    iter_rap = iter(range(1, rabbit+1))
    for i in iter_rap:
        leap -= i
        if leap < 0:
            leap += i
            break
        rab_ans += 1
        carrots -= 1
        if carrots < 0:
            carrots += 1
            rab_ans -= 1
            leap += i
            break
    ans = [abs(rabbit-rab_ans), leap, carrots]
    if sum(ans) == 0:
        print('Ahhahaha')
    else:
        print(*ans)
 
 
peko(int(input()), int(input()), int(input()))