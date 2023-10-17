"""Bill"""
def calbill(num):
    """calculate total of vat service food and drink"""
    service = 0.1*num
    if service > 1000:
        service = 1000
    if service < 50:
        service = 50
    vat = (service+num)*0.07
    print("%.2f" % (vat+service+num))
calbill(int(input()))
