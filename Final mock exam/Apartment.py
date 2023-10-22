"""apartment"""
def find_rent(aaa, bbb, ccc, ddd, eee):
    """aprt"""
    max_d = max((((aaa-ccc)*ddd)*-1 + bbb), bbb-((bbb//ddd)*ddd))
    if max_d == 0:
        max_d = ddd
    print(max_d*aaa)
    print(aaa)


find_rent(int(input()), int(input()), int(input()), int(input()), int(input()))
