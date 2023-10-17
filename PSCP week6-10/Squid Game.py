"""Squid game"""
def playsquidgame():
    """SQUID"""
    force_a = 0
    force_b = 0
    for _ in range(10):
        force_a += (int(input()))
    for _ in range(10):
        force_b += (int(input()))
    if force_a < force_b:
        print("A")
    elif force_a > force_b:
        print("B")
    else:
        print("AB")
playsquidgame()
