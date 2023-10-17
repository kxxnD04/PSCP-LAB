"""HowLong"""
def howlong(number):
    """len but not use len"""
    value_x = 10
    ans = 1
    while True:
        if abs(number) < value_x:
            print(ans)
            break
        else:
            value_x *= 10
            ans += 1
howlong(int(input()))
