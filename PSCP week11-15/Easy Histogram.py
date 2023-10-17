"""Easy Histrogram(no count)"""
def easy(txt):
    """gogogogo"""
    txt.sort(key=lambda x: ord(x) + ((32.1 if x.isupper() else 0)))
    blank = ""
    for char in txt:
        num = 0
        for i in txt:
            if i == char:
                num += 1
        if char not in  blank:
            print("{} = {}".format(char, num))
        blank += char
easy(list(input().replace(' ', '')))
