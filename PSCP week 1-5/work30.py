"""D1"""
def main(time):
    """ใช้เวลาเยอะแค่ไหนก็ตัดใจจากเธอไม่ได้ซักทีV2"""
    day, hour, mnt, sec = time // 86400, time % 86400 // 3600, time % 86400 % 3600 // 60, time % 60
    if day > 9999:
        print("ERR_:__:__:__")
    elif day <= 9999:
        day = str(day).zfill(4)
        hour = str(hour).zfill(2)
        mnt = str(mnt).zfill(2)
        sec = str(sec).zfill(2)
        print(day+":"+str(hour)+":"+str(mnt)+":"+str(sec))
main(int(input()))
