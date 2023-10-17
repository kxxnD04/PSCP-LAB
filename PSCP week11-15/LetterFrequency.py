"""LetterFrequency"""
def letterfrequency():
    """find most letter used"""
    txt = input().strip().replace(" ", "").lower()
    check_txt = []
    for i in txt:
        if i.isalpha() and i not in check_txt:
            check_txt.append([txt.count(i), i])
    check_txt.sort(reverse=True)
    print((check_txt[0])[1])

letterfrequency()
