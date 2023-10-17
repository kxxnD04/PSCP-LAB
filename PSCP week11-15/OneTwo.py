"""OneTwo"""
def onetwo(num):
    '''onetwothreefourfive I LOVE U!!!'''
    return str(num) if num == 1 or num == 2 else str(onetwo(num-1))+str(onetwo(num-2))
print(onetwo(int(input())))
