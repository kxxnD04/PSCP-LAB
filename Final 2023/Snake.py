"""Snake"""
from json import loads as l
def main():
    """Snake 17:16 - 17:48"""
    players = int(input())
    dic = {i: 1 for i in range(1, players + 1)}
    special_move = {3:21, 8:30, 28:84, 58:77, 75:86, 80:100, 90:91, 17:13, 52:29,
57:40, 62:22, 88:18, 95:51, 97:79}
    winner = []
    lis = l(input())
    while lis:
        for p in dic:
            if not lis:
                break
            if dic[p] < 100:
                dic[p] += lis.pop(0)
                dic[p] = special_move.get(dic[p], dic[p])
                if dic[p] >= 100:
                    winner += [p]
        if len(winner) == players:
            break
    if winner:
        print(*winner)
    else:
        print(-1)
    not_win = list(filter(lambda x: x[1] < 100, dic.items()))
    if not_win:
        not_win.sort(key=lambda x: (-x[1], -x[0]))
        for i,_ in not_win:
            print(i, end=' ')
main()
