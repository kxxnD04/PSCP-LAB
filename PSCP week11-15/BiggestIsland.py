"""BiggestIsland"""
MEM_ = {}
def eight_di(list1, row, col, count):
    """check island for 8 directions"""
    list1[row][col] = '-1'
    if list1[row-1][col-1] == '1':
        MEM_[count] += 1
        list1 = eight_di(list1, row-1, col-1, count)
    if list1[row-1][col] == '1':
        MEM_[count] += 1
        list1 = eight_di(list1, row-1, col, count)
    if list1[row-1][col+1] == '1':
        MEM_[count] += 1
        list1 = eight_di(list1, row-1, col+1, count)
    if list1[row][col-1] == '1':
        MEM_[count] += 1
        list1 = eight_di(list1, row, col-1, count)
    if list1[row][col+1] == '1':
        MEM_[count] += 1
        list1 = eight_di(list1, row, col+1, count)
    if list1[row+1][col-1] == '1':
        MEM_[count] += 1
        list1 = eight_di(list1, row+1, col-1, count)
    if list1[row+1][col] == '1':
        MEM_[count] += 1
        list1 = eight_di(list1, row+1, col, count)
    if list1[row+1][col+1] == '1':
        MEM_[count] += 1
        list1 = eight_di(list1, row+1, col+1, count)
    return list1

def island_count(line1, count=0):
    """main function to count island"""
    list1 = [['0' for _ in range(line1[1]+2)]]
    for _ in range(line1[0]):
        val = ['0']
        in_ = input().split()
        val.extend(in_)
        val.append('0')
        list1.append(val)
    list1.append(['0' for _ in range(line1[1]+2)])
    for rows in range(1, len(list1)-1):
        for col in range(1, line1[1]+1):
            if list1[rows][col] == '1':
                count += 1
                MEM_[count] = 1
                list1 = eight_di(list1, rows, col, count)
    print(max(MEM_.values()))

island_count([int(i) for i in input().split()])
