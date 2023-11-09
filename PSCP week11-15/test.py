num = int(input())
check = True
def diviser(num):
    ans = []
    for i in range(2, (num+1)//2):
        if num%i == 0:
            ans.append((i, int(num/i)))
    return sorted(ans, key=lambda x: x[0])[0]

if num in range(0, 2):
    print('0 = 0 * 0' if num == 0 else '1 = 1 * 1')
else:
    for i in range(2, int(num**0.5)+1, 1):
        if num%i == 0:
            check = False
            ans = diviser(num)
            print(num, '=', ans[0], 'x', ans[1])
            break

if check == True:
    print(num, 'is prime')