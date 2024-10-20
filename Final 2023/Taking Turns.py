"""Taking turn"""
from json import loads as l
def main():
    """Taking Turn 16:11 - 16:23"""
    lis = l(input())
    ans = []
    state = [-1, 0]
    front = 0
    swap = 0
    for _ in range(len(lis)):
        ans += [lis.pop(state.pop(0))]
        swap += 1
        if swap == 2 and not front:
            state = [0, -1]
            swap = 0
            front = 1
        elif swap == 2 and front:
            state = [-1, 0]
            swap = 0
            front = 0
    print(ans)
main()
