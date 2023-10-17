"""Largest Number"""
def findm_ax(num1, num2):
    """find max value"""
    if num1 == num2:
        rest = num2
    elif num1 > num2:
        rest = num1
    else:
        rest = num2
    return rest
def main(num1, num2, num3):
    """50"""
    var1 = int(str(num1)+str(num2)+str(num3))
    var2 = int(str(num1)+str(num3)+str(num2))
    var3 = int(str(num2)+str(num1)+str(num3))
    var4 = int(str(num2)+str(num3)+str(num1))
    var5 = int(str(num3)+str(num2)+str(num1))
    var6 = int(str(num3)+str(num1)+str(num2))
    find1 = findm_ax(var1, var2)
    find2 = findm_ax(find1, var3)
    find3 = findm_ax(find2, var4)
    find4 = findm_ax(find3, var5)
    find5 = findm_ax(find4, var6)
    print(find5)
main(str(input()), str(input()), str(input()))
