"""SuperMarketV2"""
def market(nnn, aaa, bbb, ccc):
    """I think its gonna timeout for sure LOL"""
    lis = sorted([int(input()) for _ in range(nnn)])
    opt1 = (sum(lis)*((100-bbb)/100)*(sum(lis) >= aaa)) + (sum(lis)*(sum(lis) < aaa))
    opt2 = (sum(lis)-max(lis))+(max(lis)*((100-ccc)/100))
    opt3 = map(lambda x: x*((100-bbb)/100) if x >= aaa else x, \
[lis[i]*((100-ccc)/100) + sum(lis) - lis[i] for i in range(len(lis))])
    print(int(min(opt1, opt2, min(opt3))))
market(*[int(input()) for _ in range(4)])
