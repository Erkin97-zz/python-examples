one_element_list = [3, 3, 4, 3, 5, 12, 24, 55] #
# list[(-i)] => list[len(list) - i]
print(one_element_list[-1])
print(one_element_list[len(one_element_list) - 1])

# how to know size of list
# list can contain any types of variable
names = ["Erkin", "Matkaziev", "Azhar", "Baktygul", "Maksat", "Papti", 12, True, 12.4]
print(len(names))

# slice
print(names)
print(names[2:5:2])
names[2:5:2] = ["Maksta", "Azhar"]
print(names)

# operations
list1 = [2, 4, 5]
list2 = [5, 3, 1]
list3 = list1 + list2
list4 = list1 * 3
print(list4)