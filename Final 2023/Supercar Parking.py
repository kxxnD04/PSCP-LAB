"""Supercar Parking"""
def main():
    """Supercar Parking 16:38 - 16:43"""
    lis = list("X" + input().strip() + "X")
    ans = 0
    for i in range(1, len(lis) - 1):
        if lis[i] == '0' and (lis[i-1] in '0X') and (lis[i+1] in '0X'):
            ans += 1
            lis[i] = '1'
    print(ans)
main()
