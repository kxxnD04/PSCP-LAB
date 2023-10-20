"""113"""
TXT_ = input()
def process(txt):
    '''remove 113 from input'''
    return txt if '113' not in txt else process(txt.replace('113', ''))
print(process(TXT_))
