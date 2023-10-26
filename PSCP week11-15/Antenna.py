"""Antenna"""
import json
def antenna(rrr, list1):
    """antenna"""
    ans = 1
    if not list1:
        print(0)
    else:
        while True:
            if list1 == []:
                print(ans)
                break
            new_list = list(filter(lambda x: x > (rrr*2)+list1[0], list1))
            if new_list == []:
                print(ans)
                break
            ans += 1
            list1 = new_list
antenna(int(input()), sorted(json.loads(input().strip())))
