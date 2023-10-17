"""Stamps"""
def stamps(nnn, aaa, bbb, ccc, ddd):
    """find stamps and total money"""
    s_tamp = 0
    total = 0
    while nnn != 0:
        foodanddrink = int(input())
        checkstamp = foodanddrink
        if s_tamp >= ccc:
            foodanddrink -= ((s_tamp//ccc)*ddd)
            if foodanddrink <= 0:
                foodanddrink = 0
                if checkstamp%ddd == 0:
                    s_tamp -= ccc*(checkstamp//ddd)
                else:
                    s_tamp -= ccc*(checkstamp//ddd+1)
            else:
                s_tamp -= ((s_tamp//ccc)*ccc)
        total += foodanddrink
        if foodanddrink >= aaa:
            s_tamp += (foodanddrink//aaa)*bbb
        nnn -= 1
    print(total)
    print(s_tamp)
stamps(int(input()), int(input()), int(input()), int(input()), int(input()))
