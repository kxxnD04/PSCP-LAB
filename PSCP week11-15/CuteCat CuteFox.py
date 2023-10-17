"""CuteCat CuteFox"""
def func_sort(txt):
    """Cat is cute?, I mean Cat girl LOL"""
    return ord(txt[1][0]), int(txt[1][3:])
def count_catfox(group_list):
    """I dont love cat anymore"""
    cat = 0
    fox = 0
    for i in group_list:
        if i[1][0:3] == 'Cat':
            cat += 1
        elif i[1][0:3] == 'Fox':
            fox += 1
    return cat, fox
def catandfox(num):
    """find cat and fox"""
    import json
    group_dict = {}
    cat_check, name_check1 = False, False
    fox_check, name_check2 = False, False
    for i in range(num):
        txt = input().split(" : ")
        first = '{"'+txt[0][2:len(txt[0])-1]+'"'
        last = '"'+txt[1][1:len(txt[1])-2]+'"}'
        new_txt = first+" : "+last
        group_dict.update(json.loads(new_txt))
    group_list = list(group_dict.items())
    for i in group_list:
        if i[0] == 'Garfield':
            name_check1 = True
        if i[0] == 'Fubuki':
            name_check2 = True
    for i in group_list:
        if i[1] == 'Cat01':
            cat_check = True
        if i[1] == 'Fox01':
            fox_check = True
    if cat_check == False and name_check1 == False:
        group_list.append(('Garfield', 'Cat01'))
    if fox_check == False and name_check2 == False:
        group_list.append(('Fubuki', 'Fox01'))
    group_list.sort(key=func_sort)
    num_cat, num_fox = count_catfox(group_list)
    print("Cat : %d" % num_cat)
    print("Fox : %d" % num_fox)
    for i in group_list:
        print(i[0]+" : "+i[1])
catandfox(int(input()))
