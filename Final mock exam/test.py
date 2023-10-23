def find_rent(a, b, c, d, e):
    if a == 0:
        print(0)
        print(0)
    else:
        max_income = b * c
        rooms_with_max_income = c
        for reduction in range(d, b, d):
            current_price = b - reduction
            if current_price > 0:
                current_income = (c + min(a - c, reduction // d)) * current_price
                if current_income > max_income:
                    max_income = current_income
                    rooms_with_max_income = c + min(a - c, reduction // d)
        for increase in range(e, b, e):
            current_price = b + increase
            current_income = c * current_price
            if current_income > max_income:
                max_income = current_income
                rooms_with_max_income = c
        print(max_income)
        print(rooms_with_max_income)


# Example usage
find_rent(int(input()), int(input()), int(input()), int(input()), int(input()))  # Sample input case