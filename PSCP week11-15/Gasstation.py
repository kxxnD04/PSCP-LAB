"""Gas stations"""
def gas(distance, full_dis, list_fuel):
    """Find Minimum number of times to refuel"""
    current, fuel_count = 0, 0
    while True:
        current += full_dis
        check = list(filter(lambda x: x <= current, list_fuel))
        if check == [] or current >= distance:
            break
        else:
            current = max(check)
            fuel_count += 1
            list_fuel = list(filter(lambda x: x > max(check), list_fuel))
    print(fuel_count if current >= distance else 'depleted')
gas(float(input()), float(input()), sorted([float(input()) for _ in range(int(input()))]))
