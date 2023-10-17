"""ScaledMatrix"""
def scale(row, col, main_list):
    """Scale matrix in range [0,1]"""
    ma_x, mi_n = [], []
    for i in range(row):
        main_list.append([float(input()) for _ in range(col)])
        ma_x.append(max(main_list[i]))
        mi_n.append(min(main_list[i]))
    for lis in main_list:
        print(*list(map(lambda x: '%.2f' % ((x-min(mi_n))/(max(ma_x)-min(mi_n))), lis)))
scale(int(input()), int(input()), [])
