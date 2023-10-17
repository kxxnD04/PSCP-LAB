"""meteorite"""
def meteor(aaa, bbb, ccc):
    """shoot that meteor"""
    count = 0
    num_meteor = 1
    weigh = aaa
    if aaa == 0:
        print(0)
    elif aaa < ccc:
        print(0)
    else:
        while True:
            weigh /= bbb
            count += num_meteor
            if weigh < ccc:
                print(count)
                break
            num_meteor *= bbb
meteor(float(input()), int(input()), float(input()))
