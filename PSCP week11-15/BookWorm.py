"""BookWorm"""
def bookworm(num_test):
    """how many books can read"""
    ans_list = []
    for _ in range(num_test):
        ans = 0
        minutes = float(input())
        num_book = int(input())
        list1 = sorted([float(input()) for _ in range(num_book)])
        for i in range(len(list1)):
            minutes -= list1[i]
            if minutes < 0:
                break
            ans += 1
        ans_list.append(ans)
    print(*ans_list, sep="\n")

bookworm(int(input()))
