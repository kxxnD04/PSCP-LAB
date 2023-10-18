"""Type of sort"""


def bubble(lis):
    '''This is bubble sort'''
    num = len(lis)
    for i in range(num):
        for j in range(0, num - i - 1):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    return lis


def main():
    """main func"""
    list1 = []
    while True:
        num = input()
        if num == 'END':
            break
        list1.append(int(num))
    print(*(bubble(list1)), sep='\n')


main()
