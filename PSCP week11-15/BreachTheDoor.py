"""BreachTheDoor"""
def breachthedoor():
    """HAHAAHA"""
    group = '''~`!@#$%&^*()-_+=}{[\\]|/:;'"<>,.?'''
    group2 = '''0123456789'''
    txt = input()
    for i in group:
        if i in txt:
            txt = txt.replace(i, "")
    for i in group2:
        if i in txt:
            txt = txt.replace(i, "")
    list1 = txt.strip().split()
    for i in list1:
        if len(i) > 6:
            print(i, end=" ")
breachthedoor()
