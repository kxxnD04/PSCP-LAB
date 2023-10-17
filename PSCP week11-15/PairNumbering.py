"""PairNumbering"""
import json
def pair(list1, list2, ppp, ans=0):
    """i want to use dict but dk how tf to use it LOL"""
    for num in set([i for i in list1 if i <= ppp]):
        b_pair = ppp-num
        if b_pair in list2:
            ans += list1.count(num)*list2.count(b_pair)
    print(ans)

pair(json.loads(input()), json.loads(input()), int(input()))
