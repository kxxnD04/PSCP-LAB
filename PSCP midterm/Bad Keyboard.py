"""Bad Keyboard"""
def badkeyword(txt):
    """chage some alphabet"""
    new_txt = ""
    for i in txt:
        if i == "o":
            new_txt += "i"
        elif i == "i":
            new_txt += "o"
        elif i == "O":
            new_txt += "I"
        elif i == "I":
            new_txt += "O"
        else:
            new_txt += i
    print(new_txt)
badkeyword(str(input()))
