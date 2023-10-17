"""Pringles"""
def pringles(line1, pringle, line2, lenght):
    """string string string get princle princle princles"""
    num_prin = 0
    for i in pringle:
        if i == ")":
            num_prin += 1
    get_prin = 0
    for i in pringle:
        if i == ")":
            get_prin += 1
        lenght -= 1
        if lenght == 0:
            break
    print(get_prin)
    print("None." if get_prin == num_prin else "There are still some left.")
    print(line1)
    for i in range(len(pringle)-1):
        if pringle[i] == ")":
            if get_prin == 0:
                print(")", end="")
            else:
                print(" ", end="")
                get_prin -= 1
        else:
            print(" ", end="")
    print("|")
    print(line2)
pringles(str(input()), str(input()), str(input()), int(input()))
