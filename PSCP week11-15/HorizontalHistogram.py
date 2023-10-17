"""HorizontalHistogram"""
def horizontal():
    """look like letter frequency"""
    txt, list1 = input(), []
    for i in txt:
        if i not in list1:
            list1.append(i)
    list1.sort(key=lambda x: ord(x)-66 if x.islower() else ord(x))
    for i in list1:
        if txt.count(i) <= 5:
            print(i+" : "+"-"*txt.count(i))
        else:
            num_set = txt.count(i)//5
            if txt.count(i)%5 == 0:
                num_set -= 1
            remain = txt.count(i)-(num_set*5)
            print(i+" : ", end="")
            for i in range(num_set):
                print("-----|", end="")
            print("-"*remain)
horizontal()
