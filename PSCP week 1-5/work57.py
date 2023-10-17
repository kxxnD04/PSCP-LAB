"""HideAndSeek"""
def hideandseek(s_tart, s_top, s_tep):
    """start stop step"""
    for _ in range(s_tart, s_top, s_tep):
        print(_)
hideandseek(int(input()), int(input()), int(input()))
