"""FourDirections"""
def fourdirectionsline1(text):
    """line1"""
    for _ in text:
        print("  *  ", end=" ")
def fourdirectionsline2(text):
    """line2"""
    for i in text:
        if i == "L":
            print(" *   ", end=" ")
        elif i == "R":
            print("   * ", end=" ")
        elif i == "U":
            print(" *** ", end=" ")
        elif i == "D":
            print("  *  ", end=" ")
def fourdirectionsline3(text):
    """line3"""
    for i in text:
        if i == "L":
            print("*****", end=" ")
        elif i == "R":
            print("*****", end=" ")
        elif i == "U":
            print("* * *", end=" ")
        elif i == "D":
            print("* * *", end=" ")
def fourdirectionsline4(text):
    """line4"""
    for i in text:
        if i == "L":
            print(" *   ", end=" ")
        elif i == "R":
            print("   * ", end=" ")
        elif i == "U":
            print("  *  ", end=" ")
        elif i == "D":
            print(" *** ", end=" ")
def fourdiractionmain(text):
    """ป้ายไฟ"""
    fourdirectionsline1(text)
    print()
    fourdirectionsline2(text)
    print()
    fourdirectionsline3(text)
    print()
    fourdirectionsline4(text)
    print()
    fourdirectionsline1(text)
fourdiractionmain(input())
