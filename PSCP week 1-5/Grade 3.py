"""Grade3"""
def main(subject):
    """Grade3"""
    total = 0
    cal1 = subject
    while subject != 0:
        score = float(input())
        if score >= 95 and score <= 100:
            total += 4
        elif score >= 90 and score < 95:
            total += 3.5
        elif score >= 85 and score < 90:
            total += 3
        elif score >= 80 and score < 85:
            total += 2.5
        elif score >= 75 and score < 80:
            total += 2
        elif score >= 70 and score < 75:
            total += 1.5
        elif score >= 65 and score < 70:
            total += 1
        elif score >= 60 and score < 65:
            total += 0.5
        elif score < 60 and score >= 0:
            total += 0
        subject -= 1
    ans2 = float("%.2f" % (total/cal1))
    if ans2 > float("%.3f" % (total/cal1)):
        ans2 -= 0.01
    print("%.2f" % ans2)
main(int(input()))
