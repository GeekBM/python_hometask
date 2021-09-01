my_list = [4, 9, 6, 8, 6, 6, 10, 9, 1, 1, 4, 10, 2, 3]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)
