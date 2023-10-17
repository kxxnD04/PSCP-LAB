"""iPhone 13 Again"""
def iphone0(models, size):
    """buy iphone"""
    if models == "iPhone 13 Pro":
        check1 = 38900*(size == "128 GB")
        check2 = 42900*(size == "256 GB")
        check3 = 50900*(size == "512 GB")
        check4 = 58900*(size == "1 TB")
        total = check1+check2+check3+check4
        return total if total != 0 else "Not Available"
    elif models == "iPhone 13 Pro Max":
        check1 = 42900*(size == "128 GB")
        check2 = 46900*(size == "256 GB")
        check3 = 54900*(size == "512 GB")
        check4 = 62900*(size == "1 TB")
        total = check1+check2+check3+check4
        return total if total != 0 else "Not Available"
    else:
        return "Not Available"

def iphone1(models, size):
    """buy iphone2"""
    if models == "iPhone 13 mini":
        check1 = 25900*(size == "128 GB")
        check2 = 29900*(size == "256 GB")
        check3 = 37900*(size == "512 GB")
        total = check1+check2+check3
        print(total if total != 0 else "Not Available")
    elif models == "iPhone 13":
        check1 = 29900*(size == "128 GB")
        check2 = 33900*(size == "256 GB")
        check3 = 41900*(size == "512 GB")
        total = check1+check2+check3
        print(total if total != 0 else "Not Available")
    else:
        print(iphone0(models, size))
iphone1(input(), input())
