"""ATM"""
def atm(current):
    """ATM pressing"""
    while True:
        act = input().split()
        if act == ['END']:
            return current
        current = max((current + (act[0] == 'D')*int(act[1]) - (act[0] == 'W')*(int(act[1]))), 0)
print(atm(int(input())))
