"""apartment"""
def find_rent(aaa, bbb, ccc, ddd, eee):
    """aprt"""
    if aaa == 0:
        print('0'+'\n0')
    else:
        max_d = (bbb- (min(bbb//ddd-1 if bbb%ddd == 0 else bbb//ddd, aaa-ccc)*ddd))*(aaa != 0)
        # max_e = (((ccc-1) if ccc not in range(0, 2) else ccc)*eee)+bbb*(aaa != 0)
        start_d = ccc+((bbb-max_d)//ddd)
        loop_d = iter(range(start_d, ccc, -1))
        loop_e = iter(range(ccc, 0, -1))
        list_d = [(max_d+(start_d-i)*ddd, i) for i in loop_d]
        list_e = [(bbb+((ccc-i)*eee), i) for i in loop_e]
        ans = sorted(list_d+list_e, key=lambda x: ((x[0]*x[1]), x[1]*-1), reverse=True)
        print(ans[0][0]*ans[0][1])
        print(ans[0][1])
        print(max_d)
        print(list_d)
        print(list_e)
        print(ans)
find_rent(int(input()), int(input()), int(input()), int(input()), int(input()))
