"""Guess"""
def guess():
    """Confuse"""
    start = 0
    stop = 101
    check = False
    ans_del = []
    while True:
        con = input().split()
        if con == ['END']:
            break
        if con[0] == '=' and con[-1] == 'YES':
            start = int(con[1])
            stop = int(con[1])+1
            check = True
        elif con[0] == '=' and con[-1] == 'NO':
            ans_del.append(int(con[1]))
            check = False
        elif con[0] == '>' and con[-1] == 'YES' and check == False:
            start = int(con[1])+1
        elif con[0] == '>' and con[-1] == 'NO' and check == False:
            stop = int(con[1])+1
        elif con[0] == '<' and con[-1] == 'YES' and check == False:
            stop = int(con[1])
        elif con[0] == '<' and con[-1] == 'NO' and check == False:
            start = int(con[1])
    if check == True:
        print(start)
    else:
        ans = set([i for i in range(start, stop)])
        ans -= set(ans_del)
        print(*sorted(list(ans)))
 
guess()
