"""EuclideanDistance"""
def distance(list1, ans=0):
    """find sum of n point distance"""
    for i in range(len(list1)-1):
        ans += (((int(list1[i+1][0])-int(list1[i][0]))**2)\
            +((int(list1[i+1][1])-int(list1[i][1]))**2))**0.5
    print('%.2f' % ans)
distance([input().split() for _ in range(int(input()))])
