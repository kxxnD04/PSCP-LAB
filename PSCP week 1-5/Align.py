'''Align'''
def main():
    '''align'''
    size = int(input())
    direction = str(input())
    direction = direction.lower()
    message = str(input())
    if direction == "left":
        print(message+" "*(size-len(message)))
    elif direction == "center":
        space1 = (size-len(message))//2
        space2 = (size-len(message))%2
        print(" "*(space1+space2)+message+" "*space1)
    elif direction == "right":
        print(" "*(size-len(message))+message)
main()
