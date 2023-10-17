"""Majority"""
def major(num, people, dic):
    """show the result of vote"""
    for i in range(1, num+1):
        dic[i] = dic.get(i, 0)
    for i in range(people):
        number = int(input())
        dic[number] += 1
    highest = sorted(dic.items(), key=lambda x: x[-1])[-1]
    if highest[-1] > people/2:
        print(*highest)
    else:
        print('0', highest[-1])
major(int(input()), int(input()), {})
