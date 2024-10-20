"""Alcohol"""
def main():
    """Alcohol 15:56 - 16:05"""
    sex = input() == 'Female'
    weight = float(input())
    d_card = input() == 'Yes'
    each_cc = float(input())
    each_pal = float(input())
    num_al = int(input())
    num_hour = int(input())
    al_drink = each_pal*num_al*each_cc/100
    al_blood = [al_drink/(weight*0.68*10), al_drink/(weight*0.55*10)][sex] * 1000 - (num_hour*15)
    if d_card and al_blood <= 50:
        print("Safe")
    else:
        print("Not Safe")
main()
