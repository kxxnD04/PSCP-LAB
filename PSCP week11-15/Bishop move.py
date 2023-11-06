"""BishopMove"""
SIZE_ = [int(input()), int(input())]
def fourdirec(bishop, direc, block, enemy, target):
    """move for the king"""
    while True:
        bishop[0] += direc[0]
        bishop[1] += direc[1]
        if bishop[0] == target[0] and bishop[1] == target[1]:
            if bishop[0] == block[0] and bishop[1] == block[1] and enemy == '0':
                return False
            else:
                return True
        elif bishop[0] == block[0] and bishop[1] == block[1]:
            return False
        if bishop[0] not in range(0, SIZE_[0]) or bishop[1] not in range(0, SIZE_[1]):
            return False
def bishopmove():
    """main function"""
    bishop = (int(input()), int(input()))
    block = (int(input()), int(input()))
    enemy = input()
    target = (int(input()), int(input()))
    direc = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    ans = [fourdirec(list(bishop), direc[i], block, enemy, target) for i in range(4)]
    print('No' if True not in ans and bishop != target else 'Yes')
bishopmove()
