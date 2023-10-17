"""ปีอธิกสุรทิน"""
def main(num1):
    """42"""
    if num1%4 == 0:
        if num1 in (1700, 1800, 1900, 2100):
            print("No")
        else:
            print("Yes")
    else:
        print("No")
main(int(input()))
