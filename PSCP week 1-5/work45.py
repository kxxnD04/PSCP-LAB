"""PlanABCDEFG"""
def main(option, num1, num2, num3):
    """44"""
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if option == "Ascend":
        print("%.2f, %.2f, %.2f" % (num1, num2, num3))
    elif option == "Descend":
        print("%.2f, %.2f, %.2f" % (num3, num2, num1))
main(str(input()), float(input()), float(input()), float(input()))
