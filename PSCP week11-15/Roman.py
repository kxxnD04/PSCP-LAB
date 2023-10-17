"""Roman"""
def roman():
    """convert roman into base 10 number"""
    used_dict = {'I' : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    used_list = list(input())
    ans = 0
    if len(used_list) > 1:
        for i in range(len(used_list)):
            if i != 0 and used_dict[used_list[i]] <= used_dict[used_list[i-1]]:
                ans += used_dict[used_list[i]]
            elif i != 0 and used_dict[used_list[i]] > used_dict[used_list[i-1]]:
                ans -= used_dict[used_list[i-1]]
                ans += abs(used_dict[used_list[i]]-used_dict[used_list[i-1]])
            else:
                ans += used_dict[used_list[i]]
        print(ans)
    else:
        print(used_dict[used_list[0]])

roman()
