"""Diginity"""
def diginity():
    """plus plus plus"""
    total = 0
    while True:
        num = str(input())
        if num == "0":
            break
        if int(num) < 10:
            print(num)
        else:
            while True:
                for i in range(0, len(num)):
                    total += int(num[i])
                num = str(total)
                total = 0
                if int(num) < 10:
                    print(num)
                    break
diginity()
