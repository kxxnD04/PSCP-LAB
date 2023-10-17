"""Milk"""
def bottleofmilk(value_a, value_b, value_c, value_d):
    """find higest bottle of milk"""
    get_frombuy = value_d//value_a
    num_lid = get_frombuy
    while num_lid >= value_b and value_c > 0:
        if value_b == 0:
            break
        else:
            num_lid -= value_b
            get_frombuy += value_c
            num_lid += value_c
    print(get_frombuy)
bottleofmilk(int(input()), int(input()), int(input()), int(input()))
