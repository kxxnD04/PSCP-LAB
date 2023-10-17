"""Netflix"""
def mobile(need1):
    return 99*need1
def basic(need1):
    return 279*need1
def standard(need1):
    if need1 % 2 != 0:
        left = need1%2
        if left == 1:
        elif left == 2:
        elif left == 4:
    else:
        return 349*(need1/2)
def prenium(need1):
    if need1 % 4 != 0:
        left = need1%2
        if left == 1:
        elif left == 2:
        elif left == 3:
    else:
        return 419*(need1/4)
def netflixoption():
    txt = ""
    need1 = max(int(input()), int(input()))
    loop1 = need1
    line3 = input()
    line4 = input()
    line5 = input()
    line6 = input()
    line7 = input()
    total = min(mobile(need1), basic(need1), standard(need1), prenium(need1))
        
netflixoption()
