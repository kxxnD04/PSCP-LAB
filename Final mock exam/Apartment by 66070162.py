'''Apartment'''
from math import ceil, floor
def apartment(var):
    '''Apartment'''
    lower_priced_function = lambda n: -var[3]*n**2 + (var[1] - var[2]*var[3])*n + var[1]*var[2]
    boundary = var[0]-var[2]
    dbydn_to0_lfn = (var[1]-var[2]*var[3])/(2*var[3])
    consider = list(filter(lambda x: 0 <= x <= boundary, [0, boundary, ceil(dbydn_to0_lfn),\
                                                          floor(dbydn_to0_lfn)]))
    to_value = list(map(lower_priced_function, consider))
    highest_of_lower = sorted((zip(to_value, map(lambda x: var[2]+x, consider))),\
                              key=lambda x: (-x[0], x[1]))[0]
 
    upper_priced_function = lambda n: -var[4]*n**2 + (var[2]*var[4]-var[1])*n + var[1]*var[2]
    boundary = max(0, var[2] - 1)
    dbydn_to0_ufn = (var[2]*var[4]-var[1])/(2*var[4])
    consider = list(filter(lambda x: 0 <= x <= boundary, [0, boundary, ceil(dbydn_to0_ufn),\
                                                          floor(dbydn_to0_ufn)]))
    to_value = list(map(upper_priced_function, consider))
    highest_of_upper = sorted((zip(to_value, map(lambda x: var[2]-x, consider))),\
                              key=lambda x: (-x[0], x[1]))[0]

    chose = sorted([highest_of_lower, highest_of_upper], key=lambda x: (-x[0], x[1]))[0]
    print(*chose, sep="\n")
apartment([int(input()) for _ in range(5)])
