"""Area"""
AREA_ = [input() for _ in range(int(input()))]
print(sum(list(map(lambda x: len(x) - x.count(' '), AREA_))))
