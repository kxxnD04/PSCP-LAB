"""Reachability"""
import json
def reach(node, start):
    """reach"""
    loop = [start]
    ans = [start]
    while loop:
        check = [i for i in node[loop.pop()] if i not in ans]
        ans += check
        loop += check
    print(sorted(list(set(ans))))
reach(dict(json.loads(input().replace("'", '"').strip())), input().strip())
