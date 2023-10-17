"""Muddled Menu"""
def menu():
    """Cry"""
    list1 = []
    while True:
        food = input()
        if '#' in food:
            food = food.strip().split(" #")
            if food[-1] == "N":
                list1.append(food[0])
            else:
                list1.insert(int(food[-1])-1, food[0])
        else:
            if food == 'DONE' or food == 'CLOSED':
                if food == 'CLOSED':
                    list1.clear()
                break
            elif food[0:10] == "Can't do: ":
                food = food.split(": ")
                list1.remove(str(food[-1]))
            elif food == "SOMETHING'S WRONG":
                list1.clear()
    print("Full Course: {} Reversed: {}".format(list1, list1[::-1]))
menu()
