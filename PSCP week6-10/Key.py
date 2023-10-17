"""Key"""
def key13(num):
    """find Key"""
    group = []
    for i in str(num):
        group.append(int(i))
    cal1 = sum(group)
    cal2 = int(str(group[-3])+str(group[-2])+str(group[-1])) *10
    cal3 = cal1 + cal2
    if len(str(cal3)) > 4:
        cal3 = str(cal3)
        print(cal3[-4]+cal3[-3]+cal3[-2]+cal3[-1])
    elif cal3 < 1000:
        print(cal3+1000)
    else:
        print(cal3)
key13(str(input()))
