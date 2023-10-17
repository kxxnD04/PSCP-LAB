"""RightArrow"""
def main(aaa, bbb):
    """make a shape of right arrow"""
    for i in range(0, bbb//2 +1):
        print((" "*(i)) + "*"*aaa)
    for i in range(bbb//2-1, -1, -1):
        print(" "*i+"*"*aaa)
main(int(input()), int(input()))
