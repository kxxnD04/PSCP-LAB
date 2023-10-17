"""Inflation"""
def inflation(price, years):
    """find latest price"""
    price *= 100
    price = int(price)
    for _ in range(years):
        price = price + ((price*381)//10000)
    print("%d.%02d" % ((price//100), price%100))
inflation(float(input()), int(input()))
