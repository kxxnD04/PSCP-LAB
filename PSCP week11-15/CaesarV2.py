"""CaesarV2"""
def caesar2(txt):
    """how many words in English LOL"""
    words = ('The ', ' the ', 'cat', ' dog ', ' and ', ' have ', ' that ', ' is ', ' am ', ' are ')
    for i in range(0, 26):
        new_txt = ""
        value_s = i
        check = 0
        for char in txt:
            if char.isalpha():
                if char.islower():
                    new = ord(char)+value_s
                    new += (-26*(new > 122))
                    new_txt += chr(new)
                else:
                    new = ord(char)+value_s
                    new += (-26*(new > 90))
                    new_txt += chr(new)
            else:
                new_txt += char
        for i in words:
            if i in new_txt:
                check += 1
        if check >= 1:
            print(new_txt)
            break
caesar2(input())
