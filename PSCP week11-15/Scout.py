"""Scout"""
def scount(num):
    """scount"""
    for _ in range(num):
        test, ans = [int(i) for i in input().split()], []
        for num in sorted([int(i) for i in input().split()]):
            ans.append(num)
            if len(ans) > test[1] or sum(ans) > test[2]:
                del ans[-1]
                break
        print(len(ans))
scount(int(input()))
