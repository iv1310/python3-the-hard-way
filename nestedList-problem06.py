"""
Given two lists list1 and list2, check if list2 is a subset of lsit1 and return True or False accordingly.

Input : list1 = [[2, 3, 1], [4, 5], [6, 8]]
        list2 = [[4, 5], [6, 8]]
Output : True

Input : list1 = [['a', 'b'], ['e'], ['c', 'd']]
        list2 = [['g']]
Output : False
"""

def checkSubset(list1, list2):
    exist = True
    for i in list2:
        if i not in list1:
            exist = False
    return exist

def checkSubsetusingset(list1, list2):
    temp1 = []
    temp2 = []
    for i in list1:
        temp1.append(i)
    for j in list2:
        temp2.append(j)
    return set(temp2) < set(temp1)

def checkSubsetuingall(list1, list2):
    return all(x in list1 for x in list2)
list1 = [[2, 3, 1], [4, 5], [6, 8]]
list2 = [[4, 5], [6, 8]]
list3 = [['a', 'b'], ['e'], ['c', 'd']]
list4 = [['g']]

print(checkSubset(list1, list2))
print(checkSubset(list3, list4))
