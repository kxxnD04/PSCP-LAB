"""Day2011"""
def day2011(days, months):
    """Day2011"""
    month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day_dict = {1:'Saturday', 2:'Sunday', 3:'Monday',\
4:'Tuesday', 5:'Wednesday', 6:'Thursday', 0:'Friday'}
    total_days = sum(month_dict.get(i, 0) for i in range(1, months)) + days
    print(day_dict[total_days%7])
day2011(int(input()), int(input()))
