"""Diamond"""
def diamond(num):
    """make diamond shape"""
    for i in range(num):
        for j in range(num):
            if i == num//2 or j - i == num//2 or i + j == num//2 \
            or i - j == num//2 or j+i == num+(num//2)-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
diamond(int(input()))
