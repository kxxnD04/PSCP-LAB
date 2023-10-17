"""RuleofThree"""
def ruleofthree(nnn):
    """find the best value"""
    price0 = (float(input()))
    weight0 = (float(input()))
    while nnn-1 != 0:
        price = (float(input()))
        weight = (float(input()))
        total_weight = weight*weight0
        if (total_weight//weight)*price < (total_weight//weight0)*price0:
            weight0, price0 = weight, price
        elif (total_weight//weight)*price == (total_weight//weight0)*price0:
            if min(price, price0) == price:
                weight0, price0 = weight, price
        nnn -= 1
    print("%.2f %.2f" % (price0, weight0))

ruleofthree(int(input()))
