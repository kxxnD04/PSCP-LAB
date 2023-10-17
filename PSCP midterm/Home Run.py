"""Home Run"""
def homerun(nnn, lenght):
    """count Home Run"""
    total = 0
    for _ in range(nnn):
        total += 1 if float(input()) < lenght else 0
    print(total)
homerun(int(input()), float(input()))
