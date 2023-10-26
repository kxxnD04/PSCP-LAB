"""[Recommended] Difference"""
import json
def diifer(first, second):
    """difffffffffff"""
    set1 = list(set(first))
    set2 = list(set(second))
    ans = []
    for i in range(len(set1)):
        ans.append((set1[i], abs(first.count(set1[i])-second.count(set1[i]))))
    for i in range(len(set2)):
        ans.append((set2[i], abs(first.count(set2[i])-second.count(set2[i]))))
    ans = list(set(ans))
    ans = sorted(list(filter(lambda x: x[1] > 0, ans)))
    if ans:
        for item in ans:
            print(*item)
    else:
        print('ONAJI DAYO!')
diifer(list(json.loads(input().replace("'", '"'))), list(json.loads(input().replace("'", '"'))))
