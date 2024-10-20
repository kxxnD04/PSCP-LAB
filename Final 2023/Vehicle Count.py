"""Vehicle Count"""
def main():
    """Vehicle Count 17:55 - 18:20"""
    ans = [0, 0, 0, 0, 0]
    first_line = input()
    lis = [list('-'*(100000))]
    line = input()
    while line != first_line:
        temp = []
        for i in line.lstrip('|').rstrip('|').split("|"):
            temp.append([" ", "x"]["x" in i])
        lis.append(temp)
        line = input()
    lis.append(list('-'*(100000)))
    for i in zip(*lis):
        temp = ''.join(list(i)).split()
        for car in temp:
            if '-' in car and 'x' in car and car.count('x') < 4:
                ans[-1] += 1
            elif car.count('x'):
                ans[min(car.count('x')-1, 3)] += 1
    print(*ans, sep='\n')
main()
