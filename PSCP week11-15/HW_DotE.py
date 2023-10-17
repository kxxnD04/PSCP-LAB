"""HW_DotE"""
def dota(players):
    """keyword is Combination(การจัดหมู่)"""
    from math import factorial
    players += 1 if players%2 != 0 else 0
    print(int((factorial(players))/((factorial(players//2))**2)))
dota(int(input()))
