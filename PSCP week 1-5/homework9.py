"""Blackjack"""
def main1(card):
    """check the point"""
    if card.isnumeric() == True:
        card = int(card)
    elif card in ("J", "Q", "K"):
        card = 10
    elif card == "A":
        card = 11
    return card

def main():
    """play blackjack"""
    num1 = int(input())
    if num1 == 2:
        num2 = main1(input())
        num3 = main1(input())
        if num2 == 11 and num2+num3 > 21:
            num1 = 1
        if num3 == 11 and num2+num3 > 21:
            num2 = 1
        print(num2 + num3)
    elif num1 == 3:
        num2 = main1(input())
        num3 = main1(input())
        num4 = main1(input())
        if num2 == 11 and num2+num3+num4 > 21:
            num2 = 1
        if num3 == 11 and num2+num3+num4 > 21:
            num3 = 1
        if num4 == 11 and num2+num3+num4 > 21:
            num4 = 1
        print(num2 + num3 + num4)
main()
