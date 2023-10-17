"""Duplicate I"""
def duplicate(num_m, num_n):
    """duplicate"""
    group1 = [input() for _ in range(num_m)]
    group2 = [input() for _ in range(num_n)]
    group3 = []
    check = 0
    for i in group1:
        if i in group2:
            group3.append(i)
            check += 1
    group3.sort(reverse=True)
    if check == 0:
        print("Nope")
    else:
        print(*group3, sep="\n")
duplicate(int(input()), int(input()))
