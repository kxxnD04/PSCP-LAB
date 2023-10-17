"""Inverter"""
def inver(txt, new=''):
    'inverter'
    for i in txt:
        if i == '1':
            new += '0'
        else:
            new += '1'
    print(int(new) if int(new) != 0 else '')
inver(input())
