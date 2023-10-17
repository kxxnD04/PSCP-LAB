"""PrasomSib"""
def prasom(txt, ans=0):
    """prasom 10"""
    for i in range(len(txt)):
        check = int(txt[i])
        for j in range(i, len(txt)-1):
            check += int(txt[j+1])
            if check == 10:
                ans += 1
                break
    print(ans)
prasom(input())
