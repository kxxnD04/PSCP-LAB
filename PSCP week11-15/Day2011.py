"""Day2011"""
def day2011(days, months):
    """Day2011"""
    month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day_dict = {1:'Saturday', 2:'Sunday', 3:'Monday',\
4:'Tuesday', 5:'Wednesday', 6:'Thursday', 7:'Friday'}
    for month in range(1, months+1):
        for day in range(1, month_dict[month]+1):
            day_process = day
            if month != 1:
                day_process += sum([month_dict[i] for i in range(1, month)])
            if day_process > 7:
                if day_process % 7 == 0:
                    day_process = day_process - (7*((day_process//7)-1))
                else:
                    day_process = day_process - (7*(day_process//7))
            ans = day_dict[day_process]
            if day == days and month == months:
                break
    print(ans)
day2011(int(input()), int(input()))
