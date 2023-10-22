"""Colors"""
def colors(rgb):
    '''color'''
    dict1 = {'bluered':'Violet', 'blueyellow':'Green', 'redyellow':'Orange',\
             'redred':'Red', 'blueblue':'Blue', 'yellowyellow':'Yellow'}
    if rgb[0] not in 'RedYellowBlue' or rgb[1] not in 'RedYellowBlue':
        print('Error')
    else:
        print(dict1[''.join(list(map(lambda x: x.lower(), rgb)))])
colors(sorted([input().strip(), input().strip()], key=lambda x: ord(x[0]))) # Blue Red Yellow
