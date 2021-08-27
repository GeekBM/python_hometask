def my_func_div_num(num_1, num_2):

    try:
        func_res = num_1 / num_2
    except  ZeroDivisionError:
        return "num_2 cannot be 0!"
    return func_res


num_1 = int(input('Enter num_1 '))
num_2 = int(input('Enter num_2 '))
func_res = my_func_div_num(num_1, num_2)

print(func_res)
