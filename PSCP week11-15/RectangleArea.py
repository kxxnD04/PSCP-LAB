"""RectangleArea"""
def recarea(rec_a, rec_b):
    """find the overlapping area of two rectangle"""
    point_x = max(rec_a[0], rec_b[0])
    point_y = max(rec_b[1], rec_a[1])
    width_x = min(rec_a[0]+rec_a[2], rec_b[0]+rec_b[2])
    heigh_y = min(rec_b[1]+rec_b[3], rec_a[1]+rec_a[3])
    ans = (max(0, width_x-point_x))*(max(0, heigh_y-point_y))
    print(ans if ans > 0 else "no overlapping")
recarea([int(i) for i in input().split()], [int(i) for i in input().split()])
