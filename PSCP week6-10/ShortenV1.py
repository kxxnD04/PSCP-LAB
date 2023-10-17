"""Shorten"""
def shorten():
    """ท้อหนัก TT"""
    group2 = ""
    continuity = False
    first_num = input()
    group2 += first_num
    while True:
        if first_num == "-1":
            group2 = "-1"
            break
        num = input()
        if num == "-1":
            break
        if int(num)-int(first_num) == 1 and continuity == False:
            group2 += "-"
            continuity = True
        elif int(num)-int(first_num) != 1 and not group2.endswith("-"):
            group2 += ", "+ num
            continuity = False
        elif int(num)-int(first_num) != 1 and group2.endswith("-"):
            group2 += first_num+", "+num
            continuity = False
        first_num = num
    if group2.endswith("-"):
        print(group2+first_num)
    elif group2 == "-1":
        print("")
    else:
        print(group2)
shorten()
