"""MAC"""
def valid1(txt):
    """check for VALID1"""
    alphacheck = "ABCDEFabcdef"
    num = 2
    checkvalid1 = True
    checkvalid2 = True
    if len(txt) == 17:
        for i in range(len(txt)):
            if i == num:
                checkvalid2 = False if txt[i] != "-" else True
                num += 3
            elif txt[i].isdigit() == False and txt[i] not in alphacheck:
                checkvalid1 = False
        if checkvalid1 == True and checkvalid2 == True:
            return "VALID 1"
        else:
            return "ERROR"
    else:
        return "ERROR"
def valid2(txt):
    """check for VALID2"""
    alphacheck = "ABCDEFabcdef"
    num = 2
    checkvalid1 = True
    checkvalid2 = True
    if len(txt) == 17:
        for i in range(len(txt)):
            if i == num:
                checkvalid2 = False if txt[i] != ":" else True
                num += 3
            elif txt[i].isdigit() == False and txt[i] not in alphacheck:
                checkvalid1 = False
        if checkvalid1 == True and checkvalid2 == True:
            return "VALID 2"
        else:
            return "ERROR"
    else:
        return "ERROR"
def valid3(txt):
    """check for VALID3"""
    alphacheck = "ABCDEFabcdef"
    num = 4
    checkvalid1 = True
    checkvalid2 = True
    if len(txt) == 14:
        for i in range(len(txt)):
            if i == num:
                checkvalid2 = False if txt[i] != "." else True
                num += 5
            elif txt[i].isdigit() == False and txt[i] not in alphacheck:
                checkvalid1 = False
        if checkvalid1 == True and checkvalid2 == True:
            return "VALID 3"
        else:
            return "ERROR"
    else:
        return "ERROR"

def macdonald(txt):
    """main function"""
    if txt.count("-") == 5:
        print(valid1(txt))
    elif txt.count(":") == 5:
        print(valid2(txt))
    elif txt.count(".") == 2:
        print(valid3(txt))
    else:
        print("ERROR")
macdonald(input())
