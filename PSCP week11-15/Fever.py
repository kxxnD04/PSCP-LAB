"""Fever"""
TEM_ = float(input())
print(('No Fever'*(36 <= TEM_ < 38))+('Mild Fever'*(38 <= TEM_ < 39))\
    +('High Fever'*(39 <= TEM_ < 40))+('Very High Fever'*(TEM_ >= 40)))
