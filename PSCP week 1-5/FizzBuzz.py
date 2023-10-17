"""Fizz Buzz"""
def main(num):
    """fizzbuzz"""
    for i in range(1, num+1):
        if i % 3 == 0 and i % 15 != 0:
            print("Fizz")
        elif i % 5 == 0 and i % 15 != 0:
            print("Buzz")
        elif i % 15 == 0:
            print("FizzBuzz")
        else:
            print(i)
main(int(input()))
