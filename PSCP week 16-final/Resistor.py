"""Resistor"""
def resistor(opt):
    """resistor"""
    color = {'Black': ('0', 1), 'Brown': ('1', 10, 0.01), 'Red': ('2', 100, 0.02),\
'Orange': ('3', 1000), 'Yellow': ('4', 10000), 'Green': ('5', 100000, 0.005),\
'Blue': ('6', 1000000, 0.0025), 'Purple': ('7', 10000000, 0.0010), 'Grey': ('8', 'err', 0.0005),\
'White': ('9', "err", "err"), 'Gold': ("err", 0.1, 0.05), 'Silver': ("err", 0.01, 0.1)}
    try:
        result = int(color[opt[0]][0] + color[opt[1]][0])*color[opt[2]][1]
        print("%.4f" % (result-(result*color[opt[3]][2])))
        print("%.4f" % (result+(result*color[opt[3]][2])))
    except (ValueError, TypeError, IndexError, KeyError):
        print('Error')
resistor([input() for _ in range(4)])
