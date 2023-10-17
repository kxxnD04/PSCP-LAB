"""ping"""
def ping1to3():
    """line1 to line3"""
    pingstat = ""
    line1 = input()
    input()
    line3 = input()
    if line1[line1.find("ping ") + 5:][0].isdigit() == False:
        start = line3.find("[")
        stop = line3.find("]")
        pingstat = line3[start + 1:stop]
    else:
        pingstat = line1[line1.find("ping ") + 5:]
    return pingstat

def findnum(txt):
    """check ms in each line"""
    if "time=" in txt:
        start = int(txt.find("time=")+5)
        stop = int(txt.find("ms"))
        return int(txt[start:stop])
    else:
        return "Error"

def findnum2(txt):
    """check ms in each line(use to find avg bc of some bug)"""
    if "time=" in txt:
        start = int(txt.find("time=")+5)
        stop = int(txt.find("ms"))
        return int(txt[start:stop])
    else:
        return int(0)

def ping4():
    """main function"""
    pingip = ping1to3()
    line4 = input().replace("<1", "=0")
    line5 = input().replace("<1", "=0")
    line6 = input().replace("<1", "=0")
    line7 = input().replace("<1", "=0")
    receive = (line4+line5+line6+line7).count(pingip)
    print("Ping statistics for %s:" % pingip)
    print("    Packets: Sent = 4, Received = %d, Lost = %d (%d"\
% (receive, 4-receive, (4-receive)*25)+ "% loss),")
    groupoftime1 = [findnum(line4), findnum(line5), findnum(line6), findnum(line7)]
    groupoftime2 = [findnum2(line4), findnum2(line5), findnum2(line6), findnum2(line7)]
    for i in range(groupoftime1.count("Error")):
        groupoftime1.remove("Error")
    groupoftime = 0
    for i in range(len(groupoftime2)):
        groupoftime += groupoftime2[i]
    if receive != 0:
        high = max(groupoftime1)
        low = min(groupoftime1)
        avg = ((groupoftime) // receive)
        print("Approximate round trip times in milli-seconds:")
        print("    Minimum = %dms, Maximum = %dms, Average = %dms" % (low, high, avg))
ping4()
