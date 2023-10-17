"""BloodDonation"""
def b_donate(age, weigh, time):
    """check if u can donate"""
    if age == 17 or age in range(60, 71):
        permis = input()
    if age in range(17, 71) and weigh >= 45:
        if time == 0 and age > 55:
            print('No')
        else:
            if age == 17 or age in range(60, 71):
                if permis == 'True':
                    print('Yes')
                else:
                    print('No')
            else:
                print('Yes')
    else:
        print('No')
b_donate(int(input()), int(input()), int(input()))
