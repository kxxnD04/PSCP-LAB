"""Sequence N"""
def nshape(size):
    """print shape of N full with '*' """
    for rows in range(size):
        for coll in range(size):
            if coll == 0 or coll == size-1 or coll == rows:
                print('*', end='')
            else:
                print(" ", end='')
        print()

nshape(int(input()))
