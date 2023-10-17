"""SumOfNumber"""
def numberplus(start):
    """find sum of number till -1 or total=start"""
    total = 0
    while True:
        num = int(input())
        if num == -1:
            print(total)
            break
        total += num
        if total == start:
            print(total)
            break
numberplus(int(input()))
