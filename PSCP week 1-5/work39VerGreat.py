"""DataSpike"""
def marg(num1, num2):
    """marg"""
    if num1 == num2:
        result = num2
    elif num1 > num2:
        result = num1
    else:
        result = num2
    return result
def main():
    """main"""
    aaa = int(input())
    bbb = int(input())
    ccc = int(input())
    ddd = int(input())
    eee = int(input())
    fff = int(input())
    ggg = int(input())
    hhh = int(input())
    amarg = (marg(aaa, bbb))
    bmarg = marg(amarg, ccc)
    cmarg = marg(bmarg, ddd)
    dmarg = marg(cmarg, eee)
    emarg = marg(dmarg, fff)
    fmarg = marg(emarg, ggg)
    gmarg = marg(fmarg, hhh)
    print(gmarg)
main()