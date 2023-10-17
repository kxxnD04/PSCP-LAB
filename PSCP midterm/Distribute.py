"""Distribute"""
def distribute(money, people):
    """give money to their child"""
    total = 0
    if money < people:
        print("-1")
    else:
        if money == people*8:
            total += people
        elif money > people*8:
            total += (people-1)
        elif money < people*8:
            new_money = money - people
            total += new_money//7
            if new_money - ((new_money//7)*7) == 3 and people - (new_money//7) == 1:
                total -= 1
        print(total)

distribute(int(input()), int(input()))
