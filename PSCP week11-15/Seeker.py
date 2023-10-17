"""Seeker"""
def seeker(txt):
    """find sumof number that hide in ascii txt"""
    checknum = False
    blank, ans = "", 0
    for i in txt:
        if i.isdecimal():
            blank += i
            checknum = True
        if not i.isdecimal() and checknum == True:
            ans += int(blank)
            checknum, blank = False, ""
    if len(blank) > 0:
        ans += int(blank)
    print(ans)
seeker(input())
