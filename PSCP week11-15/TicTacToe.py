"""TicTacToe"""
def xogames(list1):
    """play X/O game"""
    check_o, check_x = False, False
    new_list = list(zip(*list1))
    if True in list(map(lambda x: x == ('O', 'O', 'O'), list1))\
or True in list(map(lambda x: x == ('O', 'O', 'O'), new_list))\
or (list1[0][0], list1[1][1], list1[2][2]) == ('O', 'O', 'O')\
or (list1[0][2], list1[1][1], list1[2][0]) == ('O', 'O', 'O'):
        check_o = True
    if True in list(map(lambda x: x == ('X', 'X', 'X'), list1))\
or True in list(map(lambda x: x == ('X', 'X', 'X'), new_list))\
or (list1[0][0], list1[1][1], list1[2][2]) == ('X', 'X', 'X')\
or (list1[0][2], list1[1][1], list1[2][0]) == ('X', 'X', 'X'):
        check_x = True
    if (check_o, check_x) == (True, True) or (check_o, check_x) == (False, False):
        print('DRAW')
    elif check_o == True:
        print('O WIN')
    elif check_x == True:
        print('X WIN')
xogames([tuple(list(input())) for _ in range(3)])
