"""MultiplyMatrixPQR"""
def multiple(ppp, qqq, rrr, ans):
    """Multiple matrix AB"""
    matrix_a = [[int(input()) for _ in range(qqq)] for _ in range(ppp)]
    matrix_b = [[int(input()) for _ in range(rrr)] for _ in range(qqq)]
    for lis in range(len(matrix_a)):
        list2 = []
        for num_b in range(rrr):
            su_m = 0
            for i in range(len(matrix_a[lis])):
                su_m += matrix_a[lis][i]*matrix_b[i][num_b]
            list2.append(su_m)
        ans.append(list2)
    for item in ans:
        print(*item)
multiple(int(input()), int(input()), int(input()), [])
