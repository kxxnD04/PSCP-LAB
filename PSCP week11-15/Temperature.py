"""TEM_perature"""
TEM_, OLD_, NEW_ = float(input()), input(), input()
TEM_ = TEM_*(OLD_ == 'C') + ((TEM_-32)/(9/5))*(OLD_ == 'F')+\
(TEM_-273.15)*(OLD_ == 'K')+ ((TEM_/(9/5))-273.15)*(OLD_ == 'R')
TEM_ = TEM_*(NEW_ == 'C') + (TEM_*(9/5)+32)*(NEW_ == 'F')+ (TEM_+273.15)*(NEW_ == 'K')+\
((TEM_+273.15)*(9/5))*(NEW_ == 'R')
print('%.2f' % TEM_)
