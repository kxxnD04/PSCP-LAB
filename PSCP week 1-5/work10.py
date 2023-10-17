"""D1"""
def main():
    """เบื่อ"""
    numa = int(input())
    numb = float(input())
    numc = str(input())
    aaa = len(str(numa))
    print(" "*(30-aaa)+str(numa))
    print(str(numa).zfill(30))
    print("%.2f"% numb)
    print("%.12f"% numb)
    print(" "*(40-len(numc))+numc)
main()
