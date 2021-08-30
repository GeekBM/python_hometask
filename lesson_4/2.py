list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [elem for num, elem in enumerate(list) if list[num] > list[num - 1]]
print(new_list)
