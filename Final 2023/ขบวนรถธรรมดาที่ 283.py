"""ขบวนรถธรรมดาที่ 283"""
def main():
    """ขบวนรถธรรมดาที่ 283 16:24 - 16:37"""
    src, dst = input().split(', ')
    dis_src, dis_dst = "X", "X"

    while dis_src == "X" or dis_dst == "X":
        consider = input()
        if src == dst:
            print('0.00')
            return
        if consider == 'Done':
            break
        station, dis = consider.split(', ')
        if station == src:
            dis_src = float(dis)
        if station == dst:
            dis_dst = float(dis)
    if dis_src != "X" and dis_dst != "X":
        print(f"{abs(dis_src - dis_dst):.2f}")
    else:
        print("Error")
main()
