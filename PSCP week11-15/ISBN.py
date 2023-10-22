"""ISBN"""
def find_isbn(lis):
    """ISBN Number"""
    check = int((sum([i*lis[10-i] for i in range(10, 1, -1)])*(-1))%11)
    print('Yes' if check == lis[-1] else 'No ' + (str(check)*(check != 10) + 'X'*(check == 10)))
find_isbn([int(i) if i != 'X' else 10 for i in input().replace('-', '')])
