"""Password"""
def checkpunction(txt, r_value):
    """punction"""
    group = '''~`!@#$%&^*()-_+={ }[\\]|/:;'"<>,.?'''
    for i in txt:
        if i in group:
            r_value += 32
            break
    return r_value
def password():
    """how strong ur password"""
    from math import log2
    txt = str(input()).strip()
    r_value = 0
    for i in txt:
        if i.islower():
            r_value += 26
            break
    for i in txt:
        if i.isupper():
            r_value += 26
            break
    for i in txt:
        if i.isdigit():
            r_value += 10
            break
    r_value = checkpunction(txt, r_value)
    if int(log2(r_value**len(txt))) < 28:
        print(int(log2(r_value**len(txt))), "Very Weak", sep="\n")
    elif 28 <= int(log2(r_value**len(txt))) <= 35:
        print(int(log2(r_value**len(txt))), "Weak", sep="\n")
    elif 36 <= int(log2(r_value**len(txt))) <= 59:
        print(int(log2(r_value**len(txt))), "Reasonable", sep="\n")
    elif 60 <= int(log2(r_value**len(txt))) <= 127:
        print(int(log2(r_value**len(txt))), "Strong", sep="\n")
    elif int(log2(r_value**len(txt))) >= 128:
        print(int(log2(r_value**len(txt))), "Very Strong", sep="\n")
password()
