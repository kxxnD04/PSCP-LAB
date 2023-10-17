"""Lift"""
def safelift(people, weight):
    """lift safe check"""
    agecheck = False
    total_weight = 0
    for _ in range(people):
        agecheck = True if int(input()) >= 12 else agecheck
        total_weight += float(input())
    print("Safe" if people == 0 or (agecheck == True and total_weight <= weight)\
else "Not Safe")
safelift(int(input()), float(input()))
