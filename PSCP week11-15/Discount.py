'''Discount'''
def findprice(books):
    '''find the free books when buy n books'''
    while True:
        each = input()
        if each == 'ENTER':
            break
        books.append(int(each))
    if len(books) <= 5:
        print(sum(books))
    elif len(books) in range(6, 20):
        print(sum(sorted(books)[len(books)//5:]) if len(books) not in range(15, 20) else\
        sum(sorted(books)[2:]))
    else:
        print(sum(sorted(books)[len(books)//5:]))
findprice([])
