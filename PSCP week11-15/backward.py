'''backward'''
def back():
    '''backwards'''
    list1 = []
    while True:
        meassage = input()
        if meassage == "NULL":
            break
        list1.append(meassage)
    for i in range(1, len(list1)+1):
        print(list1[-1*i])
back()
