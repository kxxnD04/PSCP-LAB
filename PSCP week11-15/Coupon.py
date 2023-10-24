"""Coupon"""
def coupon(price, opt1, opt2):
    """coupon"""
    first = ('1', (price >= opt1[1])*(price-opt1[0]) + (price < opt1[1])*(price), opt1[1])
    second = ('2', (price >= opt2[1])*price*((100-opt2[0])/100) + (price < opt2[1])*price, opt2[1])
    if price < opt1[1] and price < opt2[1]:
        print('Nope')
    else:
        ans = list(sorted([first, second], key=lambda x: (x[1], x[2], int(x[0]))))
        print(ans[0][0]+' '+'%.1f' % (ans[0][1]))
coupon(float(input()), [float(i) for i in input().split()], [float(i) for i in input().split()])
