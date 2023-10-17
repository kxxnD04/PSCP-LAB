"""Kabata"""
def kabata_check(num_txt):
    """kabata"""
    for _ in range(num_txt):
        words = input()
        itkabata = 'yes'
        words = words.replace("bakka", "**").replace("baka", "ER")
        for i in range(0, len(words), 2):
            check_word = words[i:i+2]
            if check_word not in ('ka', 'ba', 'ta', '**'):
                itkabata = 'no'
        print(itkabata)
kabata_check(int(input()))
