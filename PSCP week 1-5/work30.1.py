"""D1"""
def main(time):
    """ใช้เวลาเยอะแค่ไหนก็ตัดใจจากเธอไม่ได้ซักทีV2"""
    day, hour, mnt, sec = time // 86400, time % 86400 // 3600, time % 86400 % 3600 // 60, time % 60
    if day > 9999:
        print("ERR_:__:__:__")
    elif day <= 9999:
        print("%04d:%02d:%02d:%02d"% (day, hour, mnt, sec))
main(int(input()))
