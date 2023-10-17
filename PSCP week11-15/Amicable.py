"""Amicable"""
def diviser(num):
    """im tired of ejudge"""
    return sum([(i + num//i) for i in range(1, int(num**0.5)+1) if num%i == 0])-num
def amicable(num, ans):
    """PSCP NO FUN ANYMORE TT"""
    for i in range(200, num+1):
        ami_pair = diviser(i)
        if diviser(ami_pair) == i and i != ami_pair and i not in ans:
            ans.extend([i, ami_pair])
    print(sum(ans))
amicable(int(input()), [])
