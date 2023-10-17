"""pickthem"""
def pick():
    """pick"""
    import json
    list1 = json.loads(input())
    check = 0
    for i in list1:
        if int(i)%2 == 0:
            print(i)
            check += 1
    if check == 0:
        print("Nope")
pick()
