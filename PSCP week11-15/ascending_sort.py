'''ascending'''
def ascend(list1):
    '''ascend'''
    list1.sort()
    for i in range(len(list1)):
        print(list1[i])
ascend([int(input()) for _ in range(5)])
