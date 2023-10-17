"""Imposter"""
def imposter():
    """Find imposter that ramains"""
    import json
    group = {}
    group_dead = []
    while True:
        rolls = input()
        if rolls == "Start":
            break
        group.update(json.loads(rolls))
    group2 = group.copy()
    while True:
        vote_out = input()
        if vote_out == "End":
            break
        group_dead.append(vote_out)
        group2.pop(vote_out)
    group_alive = sorted(group2.items())
    group_dead.sort()
    count_imposter = (list(group2.values())).count('Impostor')
    print(count_imposter, "Impostor Remains")
    print("***Alive***")
    for i in group_alive:
        print(i[0]+" : "+i[1])
    print('***Dead***')
    for i in group_dead:
        print(i+" : "+group[i])
imposter()
