"""Poisonous Vegetables"""
import json
def vegan(veget, spaces, times):
    """vegan"""
    garden = []
    for _ in range(veget[0]):
        row = input().strip()
        row = row.replace(' ', ", ")
        row = row.replace('][', '], [')
        garden.extend(list(json.loads('['+row+']')))
    for i in range(len(garden)):
        if garden[i][1] > spaces:
            garden[i] = ['-']
        elif garden[i][2] - garden[i][0] == 0:
            garden[i] = ['o']
        else:
            garden[i] = ['x']
    for item in range(len(garden)):
        print('[ '+garden[item][0]+' ]', end='')
        if (item+1)%veget[1] == 0 and times != -1:
            print()

vegan([int(i) for i in input().split() if i.isnumeric()], int(input()), int(input()))
