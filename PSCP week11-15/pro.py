"""Pro"""
VAL_X, VAL_Y, VAL_A, VAL_Z = int(input()), int(input()), int(input()), int(input())
print(((VAL_Z//VAL_X)*(VAL_A*VAL_Y)) + max(VAL_Z-((VAL_Z//VAL_X)*VAL_X), 0)*VAL_A)
