"""Guess"""
def guess():
    """Confuse"""
    ans = set([int(i) for i in range(0, 101)])
    while True:
        con = input().split()
        if con == ['END']:
            break
        if con[0] == '>' and con[2] == 'YES':
            ans = ans.intersection(set([int(i) for i in range(int(con[1])+1, 101)]))
        elif con[0] == '>' and con[2] == 'NO':
            ans = ans.intersection(set([int(i) for i in range(0, int(con[1])+1)]))
        elif con[0] == '<' and con[2] == 'YES':
            ans = ans.intersection(set([int(i) for i in range(0, int(con[1]))]))
        elif con[0] == '<' and con[2] == 'NO':
            ans = ans.intersection(set([int(i) for i in range(int(con[1]), 101)]))
        elif con[0] == '=' and con[2] == 'YES':
            ans = ans.intersection(set([int(con[1])]))
        elif con[0] == '=' and con[2] == 'NO':
            ans = ans.intersection(set([int(i) for i in range(0, 101) if i != int(con[1])]))
    print(*sorted(list(ans)))
guess()
