"""ValidVar"""
def checkname(name):
    """check Valid or Invalid"""
    keyword = ['if', 'else', 'elif', 'while', 'for', 'True', 'False', \
'continue', 'break', 'return', 'is', 'in', 'and', 'or', 'from', \
'as', 'pass', 'not', 'def', 'None']
    punction = '''!"#$%&'()*+,-./:;<=>?@[\\]^`{|}~'''
    validcheck = 0
    if name[0].isspace() == True:
        name = name.replace(name[0], '')
    if name[-1].isspace() == True:
        name = name.replace(name[-1], '')
    for i in name:
        if i in punction:
            validcheck += 1
    for i in name:
        if i.isspace() == True:
            validcheck += 1
    if name[0].isnumeric() == True:
        validcheck += 1
    if name in keyword:
        validcheck += 1
    if validcheck == 0:
        return "Valid"
    else:
        return "Invalid"

def loopcheckname(num):
    """ValidVar"""
    while num != 0:
        name = input()
        print(checkname(name))
        num -= 1
loopcheckname(int(input()))
