list_a = [1, 2, 3, 5, 6, 8, 9]
list_b = [3, 2, 1, 5, 6, 0]


duplicate_list = [x for x in list_a if x in list_b]
duplicate_list.sort()

print("List A     :", list_a)
print("List B     :", list_b)
print("Duplicates :", duplicate_list)
