"""T-score"""
def tscore(student, max_score):
    '''find T-score of each students'''
    list1 = [int(input()) for _ in range(student)]
    avg = sum(list1)/student *(max_score >= 0)
    sd_ = (sum([(i-avg)**2 for i in list1])/(len(list1)-1))**0.5
    ans = list(map(lambda y: '%.2f'% (50+10*(0 if sd_ == 0 else (y-avg)/sd_)), list1))
    print(*ans, sep='\n')
tscore(int(input()), int(input()))
