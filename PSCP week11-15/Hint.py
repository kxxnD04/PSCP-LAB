"""Hint"""
def hint(cond):
    """ซื้อหวยจร้าาาา"""
    ans = set(['%03d' % i for i in range(0, 1000)])
    check = ['%03d' % i for i in range(0, 1000)]
    for lab in range(3):
        if cond[lab][0] == '==':
            ans = ans.intersection(set([i for i in check if int(i[3-lab-1]) == int(cond[lab][1])]))
        elif cond[lab][0] == '!=':
            ans = ans.intersection(set([i for i in check if int(i[3-lab-1]) != int(cond[lab][1])]))
        elif cond[lab][0] == '>':
            ans = ans.intersection(set([i for i in check if int(i[3-lab-1]) > int(cond[lab][1])]))
        elif cond[lab][0] == '<':
            ans = ans.intersection(set([i for i in check if int(i[3-lab-1]) < int(cond[lab][1])]))
        elif cond[lab][0] == '>=':
            ans = ans.intersection(set([i for i in check if int(i[3-lab-1]) >= int(cond[lab][1])]))
        elif cond[lab][0] == '<=':
            ans = ans.intersection(set([i for i in check if int(i[3-lab-1]) <= int(cond[lab][1])]))
    print(*sorted(list(ans)), sep='\n')
hint([input().split() for _ in range(3)])
