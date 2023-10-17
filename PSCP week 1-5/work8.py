"""D1"""
def main(time):
    """ใช้เวลาเยอะแค่ไหนก็ตัดใจจากเธอไม่ได้ซักที"""
    day, hour, mnt, sec = time // 86400, time % 86400 // 3600, time % 86400 % 3600 // 60, time % 60
    print(day, hour, mnt, sec)
main(int(input()))
