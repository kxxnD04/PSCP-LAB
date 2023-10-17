"""Run Length Encoding"""
def encoding(text):
    """count same and close character then print them"""
    count = 1
    for i in range(0, len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            print("%d%s" % (count, text[i]), end='')
            count = 1
    print("%d%s" % (count, text[-1]), end='')
encoding(input())
