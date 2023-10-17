"""Hamming"""
TXT_1, TXT_2 = input(), input()
print(len([i for i in range(len(TXT_1)) if TXT_1[i] != TXT_2[i]]))
