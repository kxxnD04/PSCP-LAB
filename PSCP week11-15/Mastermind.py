"""Mastermind"""
def mtm(password, guess):
    """i dont even know this game LOL"""
    ans, check = [], []
    for i in range(len(guess)):
        if guess[i] == password[i]:
            ans.append('B')
            check.append(i)
    new_pass = [password[i] for i in range(len(password)) if i not in check]
    for i in range(len(guess)):
        if i not in check:
            if guess[i] in new_pass:
                ans.append('W')
            else:
                ans.append('O')
    print(''.join(sorted(ans, key=lambda x: (ord(x)- (9*(x == 'W'))))))
mtm(list(input().strip()), list(input().strip()))
