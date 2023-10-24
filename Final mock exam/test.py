"""apartment"""
from math import ceil
def find_rent(aaa, bbb, ccc, ddd, eee):
    """aprt"""
    max_d = ((bbb-(ccc*ddd))/2)
    max_d = max_d*(max_d < (aaa-ccc)*ddd and max_d >= 0)
    max_e = ((ccc*eee)-bbb)/2
    max_e = max_e*(max_e < ccc*eee and max_e >= 0)
    max_d, max_e, max_d2, max_e2 = int(max_d/ddd), ceil(max_e/eee), ceil(max_d/ddd), int(max_e/eee)
    list1d = [((ccc+max_d)*(bbb-(max_d*ddd)), ccc+max_d), \
             ((ccc+max_d2)*(bbb-(max_d2*ddd)), ccc+max_d2)]
    list1e = [((bbb+(max_e*eee))*(ccc-max_e), ccc-max_e), \
              ((bbb+(max_e2*eee))*(ccc-max_e2), ccc-max_e2)]
    # if aaa != 0:
    #     if list1d[0][0]/list1d[0][1] <= bbb:
    #         check = int((list1d[0][0]/list1d[0][1])/ddd)
    #         if (bbb-((check-ccc)*ddd))*check == list1d[0][0] and check >= ccc:
    #             list1d.append((list1d[0][0], int(check)))
    #     # if list1e[0][0]/list1e[0][1] >= bbb:
    #     #     check2 = int((list1e[0][0]/list1e[0][1])/eee)
    #     #     if (bbb-((check2-ccc)*ddd))*check2 == list1d[0][0] and check2 >= ccc:
    #     #         list1d.append((list1d[0][0], int(check2)))
    list1d += list1e
    list1d.sort(key=lambda x: (x[0], -1*x[1]), reverse=True)
    print(*list1d[0], sep='\n')
    # print(list1[5])
find_rent(int(input()), int(input()), int(input()), int(input()), int(input()))
