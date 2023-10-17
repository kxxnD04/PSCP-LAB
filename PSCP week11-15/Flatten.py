"""Flatten"""
import json

def flattern(list1):
    """need flat!"""
    new_list1 = []
    for i in list1:
        if isinstance(i, (int, float)):
            new_list1.append(i)
        else:
            new_list1.extend(flattern(i))
    return new_list1

print(sorted(flattern(json.loads(input())), reverse=True))
