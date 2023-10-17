"""Gram_v1"""
def gram_2(txt):
    """n-gram"""
    list1 = []
    for i in range(0, len(txt)-1):
        freeq = 0
        if txt[i]+txt[i+1] not in list1:
            list1.append(txt[i]+txt[i+1])
            for j in range(0, len(txt)-1):
                if txt[j]+txt[j+1] == list1[-1]:
                    freeq += 1
            list1[-1] = [txt[i]+txt[i+1], freeq]
    highest = sorted(list1, key=lambda x: x[-1])[-1][-1]
    for i in list1:
        if i[1] == highest:
            print(*i, sep='\n')
            break
gram_2(input().strip())
