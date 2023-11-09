"""Mickey"""
def mickey(nnn):
    """greedy"""
    lis1 = sorted([int(input()) for _ in range(nnn)])
    lis2 = sorted([int(input()) for _ in range(nnn)])
    print(int(max([abs(lis1[i]-lis2[i]) for i in range(len(lis1))])))

mickey(int(input()))
