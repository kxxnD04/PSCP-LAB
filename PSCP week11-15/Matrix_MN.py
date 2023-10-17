"""Matrix_MN"""
def matrix(row, col, list1):
    """show ur input matrix"""
    for i in range(row):
        list1.append([input() for _ in range(col)])
        print(*list1[i])
matrix(int(input()), int(input()), [])
