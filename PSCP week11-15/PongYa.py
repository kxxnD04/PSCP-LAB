"""PongYa"""
NUM_ = int(input())
print('PONG' if not NUM_%3 or str(NUM_)[-1] == '3' else NUM_)
