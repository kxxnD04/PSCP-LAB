"""WordSequence II"""
def wordseq2(start, stop):
    """seq2"""
    print(start)
    if len(start) <= len(stop):
        for i in range(len(stop)):
            print(stop[0:i+1]+start[i+1:])
    else:
        for i in range(len(start)):
            print(stop[0:i+1]+start[i+1:])
wordseq2(input(), input())
