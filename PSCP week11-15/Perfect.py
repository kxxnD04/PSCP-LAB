"""Perfect"""
def perfect_num(num):
    '''perfect number'''
    ans = 0
    for i in range(6, num+1, 2):
        list1 = []
        for j in range(1, int(i**0.5)+1):
            if i%j == 0:
                list1.append(j)
                list1.append(i//j)
        if sum(list1) == i*2:
            ans += i
    print(ans)
perfect_num(int(input()))
