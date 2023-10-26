"""Guess"""
def guess():
    ans = range(0,101)
    while True:
        con = input().split()
        if con == ['END']:
            break
        if con[0] == '=' and con[-1] == 'YES':
            ans = range(int(con[1]), int(con[1])+1)




guess()