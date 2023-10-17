"""Robot I"""
def main(name, age):
    """34"""
    if age < 18:
        print("%s, you can pass."%name)
    else:
        print("%s, you shall not pass."%name)
main(str(input()), float(input()))
