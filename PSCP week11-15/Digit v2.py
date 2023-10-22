"""Digit v2"""
def digit(txt):
    """digit of number"""
    check = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', \
        'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', \
        'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if 'thousand' in txt:
        print(4)
    elif 'hundred' in txt:
        print(3)
    elif len(txt) == 1 and False in list(map(lambda x: x not in check, txt)):
        print(2)
    elif len(txt) == 1 and False not in list(map(lambda x: x not in check, txt)):
        print(1)
    else:
        print(len(txt))
digit(input().split())
