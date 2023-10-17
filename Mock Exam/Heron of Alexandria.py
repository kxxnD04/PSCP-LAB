"""Heron of Alexandria"""
def hoa(aaa, bbb, ccc):
    """area of triangle"""
    sss = (aaa+bbb+ccc)/2
    print("%.3f" % ((sss*(sss-aaa)*(sss-bbb)*(sss-ccc))**0.5))
hoa(float(input()), float(input()), float(input()))
