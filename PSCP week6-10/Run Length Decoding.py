"""Run Length Decoding"""
def decoding(text):
    """print string equal to its front number"""
    num = ''
    for i in range(0, len(text)):
        if text[i].isnumeric() == True:
            num += text[i]
        else:
            print((text[i])*int(num), end='')
            num = ''
decoding(input())
