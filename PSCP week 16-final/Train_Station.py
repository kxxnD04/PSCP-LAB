"""Train Station"""
def to_minute(time: str) -> int:
    """this function may convert string format to minutes"""
    if not time:
        return None
    return int(time[:2])*60 + int(time[3:])

def main():
    """Train Station """
    platform = []
    arrival = list(map(to_minute, input().replace("[", "").replace("]", "").split(", ")))
    departure = list(map(to_minute, (input()).replace("[", "").replace("]", "").split(", ")))
    each_train = sorted(list(zip(arrival, departure)))
    for t in each_train:
        is_newplatform = 1
        for p in platform:
            if t[0] > p[-1][-1]:
                is_newplatform = 0
                p.append(t)
                break
        if is_newplatform:
            platform.append([t])
    # print(platform[0][0][0])
    print(len(platform) if platform[0][0][0] is not None else 0)
main()
