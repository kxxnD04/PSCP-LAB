"""SequenceXXX"""
def seq30(num_n, num_m):
    """I reall hate all of sequence"""
    for i in range(0, num_n):
        if i in (0, num_n-1):   #แถวบนล่าง
            for i in range(0, num_m):
                print("*"*num_n, end=" ")
            print()
        else:       # ระหว่างแถวบนล่าง
            for _ in range(0, num_m):
                for j in range(0, num_n):
                    if i == j or j == 0 or j == num_n-1 or j == num_n-1-i:
                        print("*", end="")
                    else:
                        print(" ", end='')
                print("", end=" ")
            print()
seq30(int(input()), int(input()))
