"""Filter"""
def filter_score():
    """Filter student scores"""
    import json
    txt, score, check_nope = input(), float(input()), True
    get_dict = json.loads(txt)
    get_list = list(get_dict.items())
    get_list.sort(key=lambda x: int(x[0]))
    for i in get_list:
        if float(i[1]) >= score:
            check_nope = False
            print(i[0]+"\t"+"%.2f" % float(i[1]))
    if check_nope == True:
        print("Nope")
filter_score()
