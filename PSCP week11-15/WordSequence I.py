"""WordSequence I"""
def wordsequence(txt):
    """wordseq"""
    for i in range(len(txt)):
        print(txt[0:i+1])
wordsequence(input())
