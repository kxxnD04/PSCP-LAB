"""Dancing"""
DIREC_ = {'North': (-1, 0), "Northeast": (-1, 1), 'East': (0, 1), 
    'Southeast': (1, 1), 'South': (1, 0), 'Southwest': (1, -1), 
    'West': (0, -1), 'Northwest': (-1, -1)}
def main():
    size = int(input())
    bonus = int(input())
    multiplier = int(input())
    actions = input()
    table = [[j for j in range((i-1)*size + 1, i*size+1)] for i in range(1, size + 1)]
    px, py = size//2, size//2
    
    score = 0
    while actions != 'Ultimately':
        if actions[-5::1] == 'dance':
            score += [1, multiplier][table[px][py] == bonus]
        elif actions in DIREC_:
            px = max(min(px + DIREC_[actions][0], size-1), 0)
            py = max(min(py + DIREC_[actions][1], size-1), 0)
        actions = input()
    score += [5, 5*multiplier][table[px][py] == bonus]
    print('Total point :', score)
main()
