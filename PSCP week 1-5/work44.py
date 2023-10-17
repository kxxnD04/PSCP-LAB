"""circle2"""
def main(pointx, pointy, radius, pointxn, pointyn):
    """44"""
    radisun = float(input())
    if (((pointx-pointxn)**2) + ((pointy-pointyn)**2))**0.5 >= radius+radisun:
        print("No")
    else:
        print("Yes")
main(float(input()), float(input()), float(input()), float(input()), float(input()))
