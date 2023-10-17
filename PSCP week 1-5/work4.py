"""D1"""
def main():
    """เซ็ง"""
    num1 = 492137954293754252786
    mil1 = num1
    sec1 = mil1//1000
    mil1 %= 1000
    min1 = sec1//60
    sec1 %= 60
    hou1 = min1//60
    min1 = min1%60
    day1 = hou1//24
    hou1 = hou1%24
    print(day1, hou1, min1, sec1, mil1)
main()
