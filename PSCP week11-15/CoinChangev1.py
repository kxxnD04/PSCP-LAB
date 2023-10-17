"""CoinChangev1"""
PAY_ = int(input())
print(PAY_//25+(PAY_%25)//10+((PAY_%25)%10)//5+((PAY_%25)%10)%5//1)
