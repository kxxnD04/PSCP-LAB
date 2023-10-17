"""Diamond I"""
def diamond(num_m, num_n):
    """find max diamond in each callum"""
    list1, list2 = [], []
    list_sum = []
    for _ in range(num_m):
        list1.append(input().strip().split())
    for group in range(num_n):
        for i in list1:
            list_sum.append(int(i[group]))
        list2.append(sum(list_sum))
        list_sum = []
    print(max(list2))
diamond(int(input()), int(input()))
