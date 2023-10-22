"""Factors"""


def cofac(num):
    """???"""
    list1 = []
    for i in range(2, (num//2)+1):
        if num % i == 0:
            list1.append(i)
    return list1


def factor(list1):
    """factor jaa"""
    for num in list1:
        ans = []
        mimic = num
        check = cofac(num)
        while True:
            check_fac = False
            for i in check:
                if mimic % i == 0:
                    ans.append(str(i))
                    mimic /= i
                    check_fac = True
                    break
            if check_fac == False:
                ans.append(str(int(mimic)))
                break
        if len(ans) > 1:
            ans.remove('1')
        new_ans = sorted(list(set(ans)), key=int)
        final_ans = []
        for item in new_ans:
            if ans.count(item) > 1:
                final_ans.append(item+'**'+str(ans.count(item))+" x ")
            else:
                final_ans.append(item+' x ')
        final_ans = (''.join(final_ans)).strip()
        if final_ans[-1] == 'x':
            print(final_ans[0:len(final_ans)-2])
        else:
            print(final_ans)


factor([int(input()) for _ in range(int(input()))])
