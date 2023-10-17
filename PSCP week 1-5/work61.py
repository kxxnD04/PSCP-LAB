"""BootSequence"""
def bootseq(count):
    """print 1 to count sep=_"""
    for i in range(1, count):
        print(i, end="_")
    print(count)
bootseq(int(input()))
