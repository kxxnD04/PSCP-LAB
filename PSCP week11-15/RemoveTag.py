"""RemoveTag"""
def removetag():
    """Finding Happiness"""
    txt = str(input())
    start = False
    stop = False
    new_txt = ""
    for i in range(len(txt)):
        if txt[i] == "<":
            start = True
        if txt[i] == ">" and start == True:
            start, stop = False, False
            continue
        if stop == False and start == False:
            if txt[i] != " ":
                new_txt += txt[i]
                if i != len(txt)-1:
                    if txt[i+1] == "<":
                        new_txt += " "
            elif txt[i] == " " and txt[i+1] != " ":
                new_txt += " "
    print(new_txt.split())
removetag()
