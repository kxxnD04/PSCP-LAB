"""circle1"""
def main(pointx, pointy, radius, pointxn, pointyn):
    """43"""
    if (((pointx-pointxn)**2) + ((pointy-pointyn)**2))**0.5 > radius:
        print("No")
    else:
        print("Yes")
main(float(input()), float(input()), float(input()), float(input()), float(input()))
