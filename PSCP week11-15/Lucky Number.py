# """Lucky Number"""
# def lucky(num):
#     """time out or memory error for SURE!!!"""
#     used = []
#     ans = [int(i) for i in range(1, num+1)]
#     while True:
#         if len(ans) == 1:
#             break
#         for i in ans:
#             if i not in used and i != 1:
#                 remove = i
#                 used.append(remove)
#                 break
#             else:
#                 remove = 0
#         if len(ans) < remove or remove == 0:
#             break
#         ans = [i for i in ans if (ans.index(i) +1)%remove != 0]
#         # print(ans)
#     print(*ans)

# lucky(int(input()))