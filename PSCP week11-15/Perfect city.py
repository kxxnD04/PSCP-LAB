"""Perfect city"""
from math import floor, ceil
def perci(stx, sty, endx, endy):
    """perci"""
    path = []
    if isinstance(stx, float):
        path = [(ceil(stx), sty), (floor(stx), sty)]
    else:
        path = [(stx, ceil(sty)), (stx, floor(sty))]
    ans = []
    for pox, poy in path:
        pre_ans = abs(pox-stx) + abs(poy-endy) + abs(pox-endx)
        ans.append(pre_ans)
    print('%.2f' % min(ans))
perci(*[float(input()) for _ in range(4)])
