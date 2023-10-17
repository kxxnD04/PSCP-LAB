"""stepper2"""
def stepper2(value_m, value_n):
    """print m to n"""
    step = 1 if value_m < value_n else -1
    for _ in range(value_m, value_n+step, step):
        print(int(_))
stepper2(int(input()), int(input()))
