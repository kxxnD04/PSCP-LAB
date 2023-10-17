"""Easy Histogram (No Dict)"""
def value(aaa):
    """for sort"""
    aaa = str(aaa)
    return ord(aaa) + (32.1 if aaa.isupper() else 0)
def histogram():
    """main"""
    txt = list(input().replace(" ", ""))
    txt.sort(key=value)
    for i in range(len(txt)):
        if txt[i] != txt[i-1] and len(txt) > 1:
            print(txt[i]+" = "+str(txt.count(txt[i])))
    if len(txt) == 1:
        print(txt[0]+" = "+"1")
histogram()
