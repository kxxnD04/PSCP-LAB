"""Point in Circle"""
def main(pointx, pointy, radius, pointxn, pointyn):
    """36"""
    if (((pointx-pointxn)**2) + ((pointy-pointyn)**2))**0.5 > radius:
        print("False")
    else:
        print("True")
main(float(input()), float(input()), float(input()), float(input()), float(input()))
