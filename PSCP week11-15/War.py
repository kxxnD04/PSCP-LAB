"""War"""
import json as johny
def toygodofwar(final_ans=0, compare=0):
    """Toy38 God of War Kamrammm"""
    list1 = sorted(list(johny.loads(input())), reverse=True)
    list2 = sorted(list(johny.loads(input())), reverse=True)
    for i in range(len(list2)):
        if list1[compare] > list2[i]:
            final_ans += list1[compare]
            compare += 1
    print(final_ans)
toygodofwar()
