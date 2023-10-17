"""Netflix"""
from math import ceil
def line_5(numforprocess):
    """if line 5 == yes Function"""
    if numforprocess >= 4:
        if numforprocess%4 == 0:
            print("Premium x %d" % (numforprocess/4))
            print("Total = %d THB" % 419*(numforprocess/4))
        elif numforprocess%4 == 1:
            print("Premium x %d" % (numforprocess//4))
            print("Basic x 1")
            print("Total = %d THB" % (419*(numforprocess//4)+279))
        elif numforprocess%4 == 2:
            print("Premium x %d" % (numforprocess//4))
            print("Standard x 1")
            print("Total = %d THB" % (419*(numforprocess//4)+349))
        else:
            print("Premium x %d"% ceil(numforprocess/4))
            print("Total = %d THB" % (419*ceil(numforprocess/4)))
    else:
        if numforprocess == 3:
            print("Premium x 1")
            print("Total = 419 THB")
        elif numforprocess == 2:
            print("Standard x 1")
            print("Total = 349 THB")
        elif numforprocess == 1:
            print("Basic x 1")
            print("Total = 279 THB")
def line_6(numforprocess):
    """if line 6 == yes Function"""
    if numforprocess >= 4:
        if numforprocess%4 == 0:
            print("Premium x %d" % (numforprocess/4))
            print("Total = %d THB" % (419*(numforprocess/4)))
        elif numforprocess%4 in range(1, 3):
            print("Premium x %d" % (numforprocess//4))
            print("Standard x 1")
            print("Total = %d THB" % (419*(numforprocess//4)+349))
        else:
            print("Premium x %d" % (ceil(numforprocess/4)))
            print("Total = %d THB" % (419*ceil(numforprocess/4)))
    else:
        if numforprocess <= 2:
            print("Standard x 1")
            print("Total = 349 THB")
        else:
            print("Premium x 1")
            print("Total = 419 THB")
def line_7(numforprocess):
    """if line 7 == yes Function"""
    print("Premium x %d" % ceil(numforprocess/4))
    print("Total = %d THB" % (419*ceil(numforprocess/4)))
def netflix():
    """main function"""
    numscreen = int(input())
    numdowload = int(input())
    numforprocess = max(numscreen, numdowload)
    input()
    input()
    line5 = str(input())
    line6 = str(input())
    line7 = str(input())
    if line7 == "Yes":
        line_7(numforprocess)
    elif line6 == "Yes":
        line_6(numforprocess)
    elif line5 == "Yes":
        line_5(numforprocess)
    else:
        print("Mobile x %d" % numforprocess)
        print("Total = %d THB" % (99*numforprocess))
netflix()
