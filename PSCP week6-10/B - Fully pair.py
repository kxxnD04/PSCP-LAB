"""B - Fully pair?"""
def pair(txt):
    """เศร้าจัง string ยังมีคู่ แล้วกูล่ะ TT"""
    checkpair = ""
    ans = ""
    for i in txt:
        num = txt.count(i)
        if i in checkpair:
            continue
        if num % 2 == 0:
            checkpair += i
        elif num % 2 != 0:
            ans += i
            checkpair += i
    if ans == "":
        print("fully paired")
    else:
        print(ans)

pair(input())
