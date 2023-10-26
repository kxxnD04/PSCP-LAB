"""Kangaroo"""
def max_play(aaa, bbb, ccc):
    """kangaroo"""
    print(max(ccc-bbb-1, bbb-aaa-1))
max_play(int(input()), int(input()), int(input()))
