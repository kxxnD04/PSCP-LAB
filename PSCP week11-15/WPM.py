"""WPM"""
def wpm(age, speed):
    """WPM lol"""
    print((('Very Slow'*(speed < 11)+'Slow'*(speed in range(11, 21))+\
'Average'*(speed in range(21, 31))+'Fast'*(speed in range(31, 41))+\
'Very Fast'*(speed > 40))*(age == 'Kids')) +(('Very Slow'*(speed < 26)+\
'Slow/Beginner'*(speed in range(26, 36))+'Intermediate/Average'*(speed in range(36, 46))+\
'Fast/Advanced'*(speed in range(46, 66))+'Very Fast'*(speed in range(66, 81))+\
'Insane'*(speed > 80)))*(age == 'Adults'))
wpm(input(), int(input()))
