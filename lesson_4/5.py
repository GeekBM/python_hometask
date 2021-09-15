from functools import reduce

def mult_nums(a, b):
    return a * b


new_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(mult_nums, new_list))
