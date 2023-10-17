"""Runner"""
def runner():
    """PSCP is not Fun anymore (TT)"""
    distance, people = int(input()), int(input())
    list1, time_list = [], []
    for i in range(people):
        list1.append(input().strip().split())
        time_list.append((distance-int((list1[i])[1]))/(int((list1[i])[0])))
    winner = min(time_list)
    if time_list.count(winner) > 1:
        find1, find2 = [], []
        for i in range(time_list.count(winner)):
            find1.append(time_list.index(winner)+i)
        for i in range(len(find1)):
            find2.append((list1[find1[i]]))
            find2[i].append(find1[i])
        find2.sort(reverse=True)
        print(((find2[0])[-1])+1)
    else:
        print(time_list.index(winner)+1)
runner()
