"""Lotto"""
def lottery(first, second, third1, third2, third3):
    """find money"""
    third4 = input()
    urlotto = input()
    money = 0
    if urlotto == first:
        money += 6000000
    if first == "000000" and (urlotto == "000001" or urlotto == "999999"):
        money += 100000
    elif first == "999999" and (urlotto == "000000" or urlotto == "999998"):
        money += 100000
    else:
        if "%06d" % (int(urlotto)) == "%06d" % (int(first)-1)\
or "%06d" % (int(urlotto)) == "%06d" % (int(first)+1):
            money += 100000
    if urlotto[-2:] == second:
        money += 2000
    if urlotto[0:3] == third1:
        money += 4000
    if urlotto[0:3] == third2:
        money += 4000
    if urlotto[-3:] == third3:
        money += 4000
    if urlotto[-3:] == third4:
        money += 4000
    print(money)
lottery(input(), input(), input(), input(), input())
