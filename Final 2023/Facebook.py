"""Facebook"""
def main():
    """Facebook 16:44 - 16:51"""
    name = input()
    dic = {}
    while '?' not in  name:
        name1, name2 = name.split(" <-> ")
        dic[name1] = dic.get(name1, set()) | {name2}
        dic[name2] = dic.get(name2, set()) | {name1}
        name = input()
    con1, con2 = name.split(" ? ")
    mutal = dic.get(con1, set()) & dic.get(con2, set())
    if mutal:
        print(*sorted(mutal), sep='\n')
    else:
        print('No mutual friend')
main()
