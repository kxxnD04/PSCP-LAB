"""Donut"""
def main():
    """49"""
    numa = int(input())
    numb = int(input())
    numc = int(input())
    numd = int(input())
    num_donut = numb+numc
    if numc != 0:
        if numd%num_donut == 0:
            print(((numa*numb)*((numd//num_donut))), num_donut*(((numd//num_donut))))
        else:
            total3 = ((numa*numb)*((numd//num_donut)+1))
            total4 = num_donut*(((numd//num_donut))+1)
            total1 = ((numa*numb)*((numd//num_donut)) + (numa*(numd-(num_donut*(numd//num_donut)))))
            total2 = num_donut*(((numd//num_donut))) + (numd - (num_donut*(((numd//num_donut)))))
            if total1 < total3:
                print(total1, total2)
            elif total1 > total3:
                print(total3, total4)
            elif total1 == total3:
                print(total3, total4)
    elif numc == 0:
        print((numa*numd), numd)
main()
