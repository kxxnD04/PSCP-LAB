"""BusStop I"""
def busstop(maxpeople, bus_stop):
    """count how many people that drop to their station"""
    ans = 0
    list1, list2 = [], []
    for _ in range(bus_stop):
        list1.append(input().strip().split())
    list1.sort(key=lambda x: int(x[0]))
    for i in list1:
        del i[0]
    for station in range(1, bus_stop+1):
        if station != 1 and len(list2) > 0:
            if str(station) in list2:
                for _ in range(list2.count(str(station))):
                    list2.remove(str(station))
                    ans += 1
        for i in list1[station-1]:
            if int(i) > station and len(list2) < maxpeople:
                list2.append(i)
    print(ans)

busstop(int(input()), int(input()))
