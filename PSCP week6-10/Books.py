"""Books"""
def books(nnn, kkk, xxx, yyy):
    """how many days to read all nnn books with each kkk pages"""
    from math import ceil
    pages = kkk
    day_count = 0
    checktimeout = False
    while nnn != 0:
        if ceil(kkk*(xxx/yyy)) >= kkk:
            checktimeout = True
            break
        pages -= ceil(kkk*(xxx/yyy))
        day_count += 1
        xxx += 1
        yyy += 1
        if pages <= 0:
            nnn -= 1
            pages = kkk
    if checktimeout == True:
        day_count += nnn
    print(day_count)
books(int(input()), int(input()), int(input()), int(input()))
