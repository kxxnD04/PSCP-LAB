"""Elo"""
def elo(ra_value, rb_value, choice):
    """calculate Elo rating system""" #Ti 12 Talon champion
    if choice == "A":
        print("%.2f" % (1/(1+(10**((rb_value-ra_value)/400)))))
    elif choice == "B":
        print("%.2f" % (1/(1+(10**((ra_value-rb_value)/400)))))
elo(int(input()), int(input()), input())
