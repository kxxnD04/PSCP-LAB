"""Palindrome"""
def palindrome(nnn, times):
    """time in palindrome"""
    times = times.replace(":", "")
    times = "%03d" % (int(times)+1)
    while nnn != 0:
        if times == times[-1::-1]:
            if len(times) == 3:
                print(times[0]+":"+times[1]+times[2])
            elif len(times) == 4:
                print(times[0]+times[1]+":"+times[2]+times[3])
            nnn -= 1
            times = "%03d" % (int(times)+1)
        else:
            times = "%03d" % (int(times)+1)
            if times[-2] == "6":
                if len(times) == 3:
                    times = str(int(times[0])+1)+"0"+"0"
                elif len(times) == 4:
                    times = str(int(times[0:2])+1)+"0"+"0"
                if times[0:2] == "24":
                    times = 0
            times = "%03d" % int(times)
palindrome(int(input()), input())
