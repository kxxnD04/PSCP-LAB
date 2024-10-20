"""Debaratna Road"""
def main(kilo: float):
    """Debaratna Road 15:51 - 15:54"""
    if kilo > 58.855 or kilo < 0:
        print("InValid")
    elif kilo <= 5.032:
        print("Bangkok")
    elif kilo <= 35.477:
        print("Samut Prakarn")
    elif kilo <= 52.900:
        print("Chachoengsao")
    else:
        print("Chon Buri")
main(float(input()))
