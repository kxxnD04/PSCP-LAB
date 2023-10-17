"""iPad Air"""
def ipad(color, cap, opt):
    """Cost of ipad air or print Not Available"""
    mem = {('64', 'Wi-Fi'): 19900, ('256', 'Wi-Fi'): 24900, \
           ('64', 'Wi-Fi + Cellular'): 24400, ('256', 'Wi-Fi + Cellular'): 29400}
    if color not in ('Space Gray', 'Silver', 'Green', 'Rose Gold', 'Sky Blue'):
        print('Not Available')
    else:
        print(mem.get((cap, opt), 'Not Available'))
ipad(input(), input(), input())
