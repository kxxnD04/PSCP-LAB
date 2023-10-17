"""Bonus"""
def bonus(rents, years, months):
    """bonus"""
    years += 1*(1 if months >= 10 else 0)
    years = 20 if years > 20 else years
    total = rents*years
    total = (1000000 if total > 1000000 else total)
    total = (5000 if total < 5000 else total)
    print(total)
bonus(int(input()), int(input()), int(input()))
