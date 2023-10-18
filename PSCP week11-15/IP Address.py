"""IP Address"""
def address(txt):
    """check valid or Invalid ip4 address"""
    check1 = map(lambda x: x.isnumeric() and int(x) <= 255, txt)
    print('Invalid IPv4 address' if False in check1 or len(txt) != 4 \
          else '.'.join(list(map(lambda x: str(int(x)), txt))))
address(input().split('.'))
