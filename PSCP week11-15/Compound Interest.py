"""Compound Interest"""
def compound(current, interest, times):
    """Compound Interest"""
    for _ in range(times):
        current += current*(interest/100)
    print('%.2f' % current)
compound(int(input()), float(input()), int(input()))
