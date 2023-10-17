"""Solar System"""
def findhot(left, right): #when sun is not the first and last
    """HHH"""
    hot = ""
    loop = 0
    left, right = str(left), str(right)
    loop += (-1)*len(left)
    if loop == -2:
        loop = -3
    for i in range(-2, loop, -1):
        if left[i] == " ":
            break
        hot += left[i]
    hot = hot[::-1]
    if right.count(" ") == 1:
        hot = hot + " " + right[1:]
    else:
        hot = hot + " " + right[1:right.find(" ", 1)]
    return hot
def findcool(left, right): #when sun is not the first and last
    """Why you so cold?"""
    left, right = str(left), str(right)
    cool = ""
    cool2 = ""
    if left.count(" ") < right.count(" "):
        for i in range(-2, -1*len(right), -1):
            if right[i] == " ":
                break
            cool += right[i]
        cool = cool[::-1]
    elif left.count(" ") > right.count(" "):
        cool += left[1:left.find(" ", 1)]
    else:
        cool += left[1:left.find(" ", 1)] +" "
        for i in range(-2, -1*len(right), -1):
            if right[i] == " ":
                break
            cool2 += right[i]
        cool2 = cool2[::-1]
        cool += cool2
    return cool
def mainfindhotandcool():
    """Leave me aloneeee:("""
    txt = input()
    hot = ""
    cool = ""
    num = txt.count(" ")
    txt = " " + txt + " "
    left = txt[0:txt.find(" Sun ")+1]
    right = txt[txt.find(" Sun ")+4:len(txt)+1]
    if num == 1:
        hot += (txt.replace("Sun", "")).replace(" ", "")
        cool += (txt.replace("Sun", "")).replace(" ", "")
    elif txt[0:5] == " Sun ":
        hot += txt[5:txt.find(" ", 5)]
        for i in range(-2, -1*len(txt), -1):
            if txt[i] == " ":
                break
            cool += txt[i]
        cool = cool[::-1]
    elif txt[-1:-6:-1] == " nuS ":
        for i in range(-6, -1*len(txt), -1):
            if txt[i] == " ":
                break
            hot += txt[i]
        hot = hot[::-1]
        cool += txt[1:txt.find(" ", 1)]
    else:
        hot += findhot(left, right)
        cool += findcool(left, right)
    print("Hot: %s" % hot)
    print("Cool: %s" % cool)

mainfindhotandcool()
