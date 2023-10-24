"""tax"""
def caltax(year, ccc):
    """cars tax"""
    base = (min(600, ccc)*0.5) + ((1200 if ccc > 1800 else ccc-600)*1.50)*(ccc > 600)\
    + max(ccc-1800, 0)*4
    base = base*0.9*(year == 6) + base*0.8*(year == 7) + base*0.7*(year == 8)+ \
    base*0.6*(year == 9) + base*0.5*(year >= 10) + base*(year < 6)
    print('%.2f' % base)
caltax(int(input()), int(input()))
