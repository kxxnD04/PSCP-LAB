"""FibonacciRecursionV1"""
def fibo(num):
    """Recursion practice"""
    return num if num == 0 or num == 1 else fibo(num-1)+fibo(num-2)
print(fibo(int(input())))
