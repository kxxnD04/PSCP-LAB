"""Cat Parade"""
def cat():
    """Cat Parade"""
    list1, list2, list3 = [], [], []
    while True:
        name = input().split(", ")
        if name == ['END']:
            break
        if name != ["IT'S A DOG"]:
            for i in name:
                list1.append(i)
        else:
            if len(list1) > 0:
                del list1[-1]
    for i in range(len(list1)):
        if list1[i] not in list3:
            list3.append(list1[i])
            list2.append(list1[i]+" "+str(i+1)+" "+str(list1.count(list1[i])))
    list2.sort()
    print(*list2, sep="\n")
cat()

