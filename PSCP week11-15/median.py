'''median'''
def median(times):
    '''median'''
    list1 = []
    for _ in range(times):
        list1.append(int(input()))
    list1.sort()
    if len(list1) % 2 == 1:
        print("%.1f"%list1[len(list1)//2])
    else:
        print("%.1f"% ((list1[len(list1)//2] + list1[(len(list1)//2)-1])/2))
median(int(input()))
