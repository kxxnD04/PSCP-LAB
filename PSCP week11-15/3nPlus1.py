"""3nPlus1"""
def greentea():
    """dont time out plz TT"""
    while True:
        num, list1 = int(input()), []
        if num == 0:
            break
        list1.append(num)
        while num != 1:
            if num%2 == 0:
                num /= 2
            else:
                num = num*3+1
            list1.append(num)
        print(len(list1))
greentea()
