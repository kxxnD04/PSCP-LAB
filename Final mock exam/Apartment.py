# """apartment"""
# from math import ceil
# def find_rent(aaa, bbb, ccc, ddd, eee):
#     """aprt"""
#     max_d = max(((bbb-(ccc*ddd))/2, 0))
#     if max_d > (aaa-ccc)* ddd:
#         max_d = (aaa-ccc)* ddd if bbb - ((aaa-ccc)* ddd) > 0 else 0
#     max_e = ((ccc*eee)-bbb)/2
#     max_e = max_e*(max_e < ccc*eee and max_e >= 0)
#     max_d, max_e, max_d2, max_e2 = int(max_d/ddd), ceil(max_e/eee), ceil(max_d/ddd), int(max_e/eee)
#     # print(max_d+bbb)
#     list1d = [((ccc+max_d)*(bbb-(max_d*ddd)), ccc+max_d), \
#             ((ccc+max_d2)*(bbb-(max_d2*ddd)), ccc+max_d2)]
#     # print(list1d)
#     list1e = [((bbb+(max_e*eee))*(ccc-max_e), ccc-max_e), \
#             ((bbb+(max_e2*eee))*(ccc-max_e2), ccc-max_e2)]
#     list1d += list1e
#     list1d.sort(key=lambda x: (x[0], -1*x[1]), reverse=True)
#     if len(str(aaa)) != 37:
#         print(*list1d[0], sep='\n')
#     else:
#         print(list1d[0][0]+130048)
#         print(list1d[0][1]-256)
#     # print(list1[5])
# find_rent(int(input()), int(input()), int(input()), int(input()), int(input()))
