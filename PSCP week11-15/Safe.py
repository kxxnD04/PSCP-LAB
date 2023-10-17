"""Safe"""
def safe(chest_key, lock):
    """Safe Key"""
    ans = 0
    for i in range(len(chest_key)):
        ans += min((abs(ord(chest_key[i])-ord(lock[i])))\
, ((ord(chest_key[i])-ord("A"))+1)+(ord("Z")-ord(lock[i]))\
, (ord("Z")-ord(chest_key[i]))+abs(ord(lock[i])-ord("A"))+1)
    print(ans)
safe(list(input()), list(input()))
