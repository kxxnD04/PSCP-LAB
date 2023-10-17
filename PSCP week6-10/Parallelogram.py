"""Parallelogram"""
def parallelogram(text):
    """print text to Parallelogram shape"""
    for i in range(0, len(text)):
        print((" "*(len(text)-i-1))+text[0:i+1])
    for i in range(1, len(text)):
        print(text[i:])
parallelogram(input())
