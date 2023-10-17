"""ProgressiveTax"""
def tax(income):
    """Find tax of thai people"""
    total_tax = 0
    if income > 4000000:
        total_tax += (((income-4000000)*0.35)*100)//100
        income = 4000000
    if income in range(2000001, 4000001):
        total_tax += (((income-2000000)*0.30)*100)//100
        income = 2000000
    if income in range(1000001, 2000001):
        total_tax += (((income-1000000)*0.25)*100)//100
        income = 1000000
    if income in range(750001, 1000001):
        total_tax += (((income-750000)*0.20)*100)//100
        income = 750000
    if income in range(500001, 750001):
        total_tax += (((income-500000)*0.15)*100)//100
        income = 500000
    if income in range(300001, 500001):
        total_tax += (((income-300000)*0.10)*100)//100
        income = 300000
    if income in range(150001, 300001):
        total_tax += (((income-150000)*0.05)*100)//100
        income = 150000
    if income in range(0, 150001):
        total_tax += 0
    print(int(total_tax))
tax(int(input()))
