"""BMIอีกละะหรอ"""
def main(weight, height):
    """37"""
    if (weight)/((height/100)**2) >= 30:
        print("Obese")
    elif 25 <= (weight)/((height/100)**2) < 30:
        print("Overweight")
    elif 18.5 <= (weight)/((height/100)**2) < 25:
        print("Normal")
    elif (weight)/((height/100)**2) < 18.5:
        print("Underweight")
main(int(input()), int(input()))
