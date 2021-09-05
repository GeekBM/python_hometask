from itertools import cycle
my_list = ['str_1', 55, 'str_2', True]
for i in cycle(my_list):
    print(i)
