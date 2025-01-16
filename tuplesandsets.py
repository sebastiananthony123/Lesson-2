sets = {34,56,22, 78 ,56,98, 34 ,23, 54,56}
print(sets)

setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of 2 said sets:")
setz = setx.intersection(sety)
print(setz)

print("--------------ARRAY----------------")

my_list = [1, 2, 3, 4, 5]

mixed_list = [1, "apple", 3,14, True]

print(my_list[0])
print(my_list[2])


my_list[0] = 10
print(my_list)

my_list.append(6)
print(my_list)

print(my_list[1:4])

print("------------HOMEWORK------------------")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

symmetric_diff = set1.symmetric_difference(set2)

print("Symmetric Difference:", symmetric_diff)

