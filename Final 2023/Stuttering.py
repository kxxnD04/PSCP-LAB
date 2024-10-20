"""Stuttering"""
def main():
    """Stuttering 16:06 - 16:10"""
    word = input().split()
    not_stutter = [0]
    for i in word:
        if i != not_stutter[-1]:
            not_stutter += [i]
    print(" ".join(not_stutter[1:]))
main()
