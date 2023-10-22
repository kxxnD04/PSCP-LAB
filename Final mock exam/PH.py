"""PH"""


def findph(num):
    """ph"""
    print(("acidic"*(0 <= num < 7))+("neutral"*(num == 7))+("akaline"*(7 < num <= 14)) +
          ("error"*(num < 0 or num > 14)))


findph(float(input()))
