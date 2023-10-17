"""SceneSwitch I"""
def scenceswitch():
    """Scenceswitch1"""
    list1, ans, daylight = [], 0, True
    while True:
        sec = input()
        if sec == "End":
            break
        list1.append(float(sec))
    for i in range(0, len(list1)):
        if i%2 == 0 and i not in (0, 1) and daylight == True:
            if list1[i]-list1[i-1] <= 6:
                ans += 1
                daylight = False
        elif i%2 == 0 and i not in (0, 1) and daylight == False:
            daylight = True
    print(ans)

scenceswitch()
