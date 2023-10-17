"""AndAgain"""
def andagain(txt):
    """find word that have 2 or more pool"""
    ans_list = []
    count = 0
    group1 = "aeiouAEIOU"
    txt = str(txt).replace(".", "").split()
    for word in txt:
        check = 0
        for j in group1:
            if j in word:
                check += word.count(j)
        if check >= 2:
            ans_list.append(word)
            count += 1
    ans_list.sort()
    if count == 0:
        print("Nope")
    else:
        print(*ans_list, sep="\n")

andagain(str(input()))
