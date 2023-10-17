"""Turnstile"""
def turnstile():
    """Count people that go through Turnstile"""
    checkpeople = ''
    countpeople = 0
    while True:
        action = input()
        checkpeople += action
        if checkpeople == 'CP':
            countpeople += 1
            checkpeople = ''
        if len(checkpeople) == 2:
            checkpeople = checkpeople[1]
        if action == "END":
            print(countpeople)
            break
turnstile()
