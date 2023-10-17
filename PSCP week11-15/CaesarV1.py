"""CaesarV1"""
def caesar(num_s, txt):
    """CAEsar"""
    new_txt = ""
    if abs(num_s) > 25:
        num_s = num_s%26 if num_s > 0 else -1*(abs(num_s)%26)
    for char in txt:
        if char.isalpha():
            if char.islower():
                new = ord(char)+num_s
                new += (-26*(new > 122)) + (26*(new < 97))
                new_txt += chr(new)
            else:
                new = ord(char)+num_s
                new += (-26*(new > 90)) + (26*(new < 65))
                new_txt += chr(new)
        else:
            new_txt += char
    print(new_txt)
caesar(int(input()), input())
