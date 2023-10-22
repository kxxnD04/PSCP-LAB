"""Hellooooo"""


def main(txt):
    """YAK CHIP HAY"""
    check = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    check2, list1 = False, []
    for char in range(-1, (len(txt)+1)*-1, -1):
        if txt[char] in check:
            same = txt[char]
            check2 = True
            break
    if check2 == False:
        print(txt)
    else:
        list2 = list(txt)
        for _ in range(txt.count(same)):
            list1.append(list2.index(same))
            list2[list2.index(same)] = '0'
        pos = (max(list1))
        print(txt[:pos]+(same*4)+txt[pos+1:len(txt)])


main(input())
