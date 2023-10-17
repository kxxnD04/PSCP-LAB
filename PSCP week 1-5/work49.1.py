"""DonutV2"""
def main(num_a, num_b, num_c, num_d):
    """อะไรกันเนี่ย"""
    num_donut = num_b + num_c
    price_donut = num_a*num_b
    num_box = num_d//num_donut
    remain_donut = num_d - (num_box*num_donut)
    if remain_donut >= num_b:
        num_box += 1
        remain_donut = 0
    print(num_box*price_donut + remain_donut*num_a, num_donut*num_box + remain_donut)
main(int(input()), int(input()), int(input()), int(input()))
