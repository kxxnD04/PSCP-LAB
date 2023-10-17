"""FibonacciRecursionV2"""
MEM_ = {0:0, 1:1} #max fibo = 20577
def fibo0(num):
    """fibo"""
    if num in MEM_:
        return MEM_[num]
    call = fibo0(num-1) + fibo0(num-2)
    MEM_[num] = call
    return call
def loop_(num, now=0):
    """im just find out that we can add MEM_ using another func"""
    if now < num:
        fibo0(now+450)
        loop_(num, now+450)
def fibo_main(num):
    """fibonacci"""
    loop_(num)
    return fibo0(num)
print(fibo_main(int(input())))

