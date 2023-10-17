"""CalculatorV2"""
def calculator(num):
    """count how many press"""
    count = 0
    if num == 1:
        print(1)
    else:
        for i in range(1, len(str(num))+1):
            num_range = range(10**(i-1), (10**i)-1)
            num_cal = ((10**i)) - (10**(i-1))
            if num in num_range:
                num_cal = (num - (10**(i-1)))+1
            count += num_cal*(1+i)
        print(count)
calculator(int(input()))
