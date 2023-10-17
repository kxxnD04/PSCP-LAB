"""ClockHands"""
def clocks(hours, minutes):
    """Check to see if the long and short hands overlap"""
    print(True if (hours*30)+(minutes/2) >= minutes*6 and \
(hours*30)+(minutes/2) - minutes*6 < 6 else False)

clocks(int(input()), int(input()))
