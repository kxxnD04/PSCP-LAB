"""Future Message"""
def main():
    """Future message"""
    message = input()
    if message.isnumeric() == True:
        print("Number")
    elif message.isupper() == True:
        print("Uppercase")
    elif message.islower() == True:
        print("Lowercase")
    elif message.istitle() == True:
        print("Title")
    elif message.isspace() == True:
        print("Space")
    else:
        print("Other")
main()
