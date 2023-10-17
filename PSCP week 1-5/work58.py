"""GraderMachine"""
def gradermac(s_tart, s_top):
    """find even number and print sum of them"""
    if s_tart%2 == 1:
        s_tart = s_tart + 1 if s_tart < s_top else s_tart - 1
    total = 0
    step = -2 if s_tart > s_top else 2
    s_top = s_top-1 if s_tart > s_top else s_top+1
    print("pass : ", end='')
    for _ in range(s_tart, s_top, step):
        total += _
        print(_, end=' ')
    print("\nSum : %d"% total)
gradermac(int(input()), int(input()))
