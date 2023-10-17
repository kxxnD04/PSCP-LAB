"""Classify"""
def classify():
    """classify but I CRY TT"""
    list1, list2 = [], []
    while True:
        data = input()[0:4]
        if data == "END":
            break
        list1.append(data)
    list1.sort()
    for i in list1:
        if (i[0:2]+" "+str(int(i[2:]))+" "+str(list1.count(i))) not in list2:
            list2.append(i[0:2]+" "+str(int(i[2:]))+" "+str(list1.count(i)))
    if len(list2) > 1:
        for word in range(len(list2)):
            if (list2[word])[0:2] == (list2[word-1])[0:2]:
                print("--"+(list2[word])[2:])
            else:
                print(list2[word])
    else:
        print(*list2)
classify()
