"""RunGame"""
LIST_ = list(map(int, input().split()))
print(abs(LIST_[0]) + sum([abs(LIST_[i]-LIST_[i+1]) for i in range(len(LIST_)-1)]) if LIST_ else 0)
