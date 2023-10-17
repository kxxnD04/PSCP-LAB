"""Phasmophobia"""
def phasmo(group, ke_y=""):
    """maybe dict can solve this one?"""
    ans = []
    evidence = {'EMF Level 5': 1, 'Ghost Writing': 2, 'Fingerprints': 3,\
                'Spirit Box': 4, 'Freezing Temperatures': 5, 'Ghost Orb': 6}
    ghost = {'135': 'Banshee', '245': 'Demon', '146': 'Jinn', '456': 'Mare', '124': 'Oni',\
    '156': 'Phantom', '346': 'Poltergeist', '123': 'Revenant', '126': 'Shade', '234': 'Spirit',\
    '345': 'Wraith', '256': 'Yurei'}
    group2 = [i for i in group if i in tuple(evidence.keys())]
    call = sorted([evidence[i] for i in group2])
    for i in call:
        ke_y += str(i)
    if len(ke_y) == 3 and ke_y in tuple(ghost.keys()):
        print(ghost[ke_y])
    elif len(ke_y) == 2:
        ans.extend([ghost[i] for i in tuple(ghost.keys()) if ke_y[0] in i and ke_y[1] in i])
        print(*sorted(ans), sep='\n')
    elif len(ke_y) == 1:
        ans.extend(ghost[i] for i in tuple(ghost.keys()) if ke_y in i)
        print(*sorted(ans), sep='\n')
    else:
        if group.count('No evidence') in range(1, 4):
            print(*(list(ghost.values())), sep='\n')
        else:
            print('Not yet discovered')
phasmo(list(set([input().strip() for _ in range(3)])))
