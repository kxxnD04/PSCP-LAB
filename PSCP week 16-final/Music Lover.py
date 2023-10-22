"""Music Lover"""
def music(list1, ans):
    """music lover"""
    for item in list1:
        if item[0] not in ans.keys():
            ans[item[0]] = [item[1].strip()]
        else:
            ans[item[0]].append(item[1].strip())
    for name, song in ans.items():
        print(name)
        print(*song, sep='\n')
music([input().split('-') for _ in range(int(input()))], {})
