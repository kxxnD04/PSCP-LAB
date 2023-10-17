"""VerticalHistogram"""
def vertical(txt):
    """VerticalHistogram (PSCP IS FUN)"""
    list1 = []
    list1.extend(list(set(txt)))
    list1.sort(key=lambda x: ord(x)-66 if x.islower() else ord(x))
    alpha = max([txt.count(i) for i in list1])
    for i in range(alpha+1):
        if i != alpha:
            print("%03d" % (alpha-i), end=" ")
            for char in list1:
                print("*" if txt.count(char) >= alpha-i else " ", end=" ")
            print()
        else:
            print("   ", end=" ")
            for i in list1:
                print(i+" ", end="")
vertical(input())
