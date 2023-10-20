"""เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที
ปกติเราก็ชอบไปทะเลอยู่แล้ว ถ้าได้ไปเที่ยวทะเลกับเธอคงจะดีมากๆเลยเนอะ
    ___แค่มีเธอไปเดินเตะคลื่นทะเลด้วยกัน No One Else___
        วันนี้เธอว่างรึเปล่า ก็ไม่ได้เป็นวันสำคัญ
    แค่อยากจะชวนให้เธอมาอยู่ และอยากจะชวนแค่เธอเท่านั้น
    ปิดรับเรื่องราวทุกอย่าง ทั้งโลกจะมีแค่เธอและฉัน
    อยากไปที่ไหนที่มีแค่เธอ ถ่ายรูปตอนเผลอให้เธอทั้งวัน

    แค่อยากขอใกล้เธอสักวัน แค่เพียงนั่งฟังเรื่องเธอได้ไหม
    อยู่กับฉันทั้งคืนถึงฟ้าสว่าง แค่เธอและฉันทำตามเสียงหัวใจ

    แค่มีเธอข้าง ๆ ในตอนตื่น
    แค่นอนดูท้องฟ้า ไปเดินเตะคลื่นทะเลด้วยกัน
    นั่งมองดูแสงจันทร์ค่อย ๆ เลือนหาย
    แค่มีเธอข้าง ๆ ให้ได้ยินเสียงที่เธอหายใจ
    แอบกระซิบเบา ๆ ว่ารักเธอ แค่มีเธอฉันยอมหมดทั้งใจ

    ที่ไหนที่เธอเคยบอก ว่าอยากจะลองไปด้วยกัน
    ขอเพียงเธอพูดว่าจะไป สุดขอบฟ้าจะห่างไกล แค่ไหนก็ไม่สำคัญ

    แค่อยากขอใกล้เธอสักวัน แค่เพียงนั่งฟังเรื่องเธอได้ไหม
    อยู่กับฉันทั้งคืนถึงฟ้าสว่าง แค่เธอและฉันทำตามเสียงหัวใจ

    แค่มีเธอข้าง ๆ ในตอนตื่น
    แค่นอนดูท้องฟ้า ไปเดินเตะคลื่นทะเลด้วยกัน
    นั่งมองดูแสงจันทร์ค่อย ๆ เลือนหาย
    แค่มีเธอข้าง ๆ ให้ได้ยินเสียงที่เธอหายใจ
    แอบกระซิบเบา ๆ ว่ารักเธอ แค่มีเธอฉันยอมหมดทั้งใจ

    เวลานี้ขอมีแค่เธอและฉัน ต่อจากนี้ขอมีแค่เธอ

    อยู่กับฉันทั้งคืนถึงฟ้าสว่าง แค่เธอและฉันทำตามเสียงหัวใจ

    แค่มีเธอข้าง ๆ ในตอนตื่น
    แค่นอนดูท้องฟ้า ไปเดินเตะคลื่นทะเลด้วยกัน
    นั่งมองดูแสงจันทร์ค่อย ๆ เลือนหาย
    แค่มีเธอข้าง ๆ ให้ได้ยินเสียงที่เธอหายใจ
    แอบกระซิบเบา ๆ ว่ารักเธอ ฉันต้องการแค่เธอคนนี้

    แค่มีเธอข้าง ๆ ในตอนตื่น
    แค่นอนดูท้องฟ้า ไปเดินเตะคลื่นทะเลด้วยกัน
    แค่มีเธอทุกวัน เท่านี้ได้ไหม
    แค่มีเธอข้าง ๆ ให้ได้ยินเสียงที่เธอหายใจ
    แอบกระซิบเบา ๆ ว่ารักเธอ เธอคนเดียวต่อจากนี้
    ฉันขอมีแค่มีเธอ...ทั้งหัวใจ
    https://www.youtube.com/watch?v=9nDjgusMmCY
                """


def deepsea(txt):
    '''find deep sea shark'''
    zone = {'BULL': 'THE SHALLOW ZONE',
            ('CHAINCAT', 'GREATWHITE', 'GUMMY', 'BLUE', 'MAKO'): 'THE TWILIGHT ZONE',
            ('FRILLED', 'GOBLIN', 'SIXGILL', 'GREENLAND', 'COOKIECUTTER'): 'THE MIDNIGHT ZONE',
            ('MEGAMOUTH'): 'THE ABYSSAL ZONE'}
    print('ZONE JAI MA KLUNG RAK DUAY KAN MAI.' if 'SHARK' not in txt else list(zone.values())\
    [list(map(lambda x: (txt.replace('SHARK', '')).strip() in x, list(zone.keys()))).index(True)])
deepsea(input().replace(' ', ''))
