'''function'''
def futaro():
    '''solution'''
    ichika = int(input())
    nino = int(input())
    miku = int(input())
    yotsuba = int(input())
    itsuki = int(input())
    percent_futaro = float(input()) / 100
    days = int(input())  #use for while count percent each other
    ichika_percent = 0
    nino_percent = 0
    miku_percent = 0
    yotsuba_percent = 0
    itsuki_percent = 0
    check = 0
    while True:
        if days == 0:
            break
        ichika_percent += (ichika / 100) * percent_futaro
        nino_percent += (nino / 100) * percent_futaro
        miku_percent += (miku / 100) * percent_futaro
        yotsuba_percent += (yotsuba / 100) * percent_futaro
        itsuki_percent += (itsuki / 100) * percent_futaro
        days -= 1
    if ichika_percent * 100 > 60:
        print("Ichika : Pass")
    else:
        print("Ichika : Fail")
        check += 1

    if nino_percent * 100 > 60:
        print("Nino : Pass")
    else:
        print("Nino : Fail")
        check += 1

    if miku_percent * 100 > 60:
        print("Miku : Pass")
    else:
        print("Miku : Fail")
        check += 1

    if yotsuba_percent * 100 > 60:
        print(yotsuba_percent)
        print("Yotsuba : Pass")
    else:
        print("Yotsuba : Fail")
        check += 1

    if itsuki_percent * 100 > 60:
        print("Itsuki : Pass")
    else:
        print("Itsuki : Fail")
        check += 1
    if check >= 3:
        print("Futaro Outtt!!!")

#โค้ดนี้จุดประสงค์คือต้องการให้เช็คว่าแต่ละคนเรียนรู้้ไปได้กี่ % ของที่ผู้สอน สอน โดยการกำหนดค่าเอง

futaro()