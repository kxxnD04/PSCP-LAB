"""SecondConverter"""
def secondconverter(kkk, sss, mmm, hhh):
    """make ur own time converter"""
    hour = (kkk%(sss*mmm*hhh))//(sss*mmm)
    minute = ((kkk%(sss*mmm*hhh))%(sss*mmm))//(sss)
    second = ((kkk%(sss*mmm*hhh))%(sss*mmm))%(sss)
    print("%d:%d:%d" % (hour, minute, second))
secondconverter(int(input()), int(input()), int(input()), int(input()))
