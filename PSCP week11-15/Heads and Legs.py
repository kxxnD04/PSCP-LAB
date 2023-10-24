"""Heads and Legs"""
def findrapandbird(aaa, bbb):
    """find rabbits and birds"""
    if aaa == 0 and bbb == 0:
        print('0 0')
    elif aaa == 0 and bbb != 0:
        print('Impossible')
    else:
        rap = (bbb-(2*aaa))/2
        if rap != int(rap) or rap < 0:
            print('Impossible')
        else:
            bird = aaa-rap
            if bird != int(bird) or bird < 0:
                print('Impossible')
            else:
                print(int(rap), int(bird))
findrapandbird(int(input()), int(input()))
