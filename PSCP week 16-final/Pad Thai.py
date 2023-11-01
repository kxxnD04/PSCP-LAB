"""Pad Thai"""
def gordonramsey():
    """กอร์ดอน แรมซี แม่งทำผัดไทยไม่เป็นเว้ย บอกเฉยๆ ไม่มีไร อิอิิอิอิอิอิอ"""
    ingradinet = ("Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", "Bean Sprouts", "Noodle",\
     "Chives", "Lime", "Egg", "Oil", "Peanuts")
    flavor = ("Sweet", "Sour", "Salty")
    ingra_add, flavor_add = [], []
    check_ingra, check_flav = True, True
    while True:
        opt = input()
        if opt == 'Cook':
            break
        if opt not in ingradinet:
            check_ingra = False
        else:
            ingra_add.append(opt)
    while True:
        fla = input()
        if fla == 'End':
            break
        if fla not in flavor:
            check_flav = False
        flavor_add.append(fla)
    if check_ingra == False:
        print("This is not Pad Thai!!!")
    elif len(set(ingra_add)) < 11:
        print("This is bad!")
    elif len(set(ingra_add)) == 11 and (not check_flav or len(set(flavor_add)) != 3):
        print("Not Bad...")
    else:
        print("Delicious!")
gordonramsey()
