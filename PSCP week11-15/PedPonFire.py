"""PedPonFire"""
def ped(group_ped, kkk, ans=0):
    """ped pon fire?""" #key is use list to count pair
    group_ped.sort()
    group_ped2 = group_ped.copy()
    for i in sorted(list(set(group_ped))):
        gas_left = kkk - i
        if gas_left != i:
            ans += group_ped2.count(gas_left)*group_ped2.count(i)
            del group_ped2[0:group_ped2.count(i)]
        else:
            num = group_ped2.count(gas_left)
            ans += num-1 if num in range(1, 3) else sum([i for i in range(num)])
    print(ans)
ped([int(input()) for _ in range(int(input()))], int(input()))
