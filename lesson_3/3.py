arg_1 = int(input('Enter arg_1 '))
arg_2 = int(input('Enter arg_2 '))
arg_3 = int(input('Enter arg_3 '))

def my_func (arg_1, arg_2, arg_3):


    if arg_2 >= arg_1 <= arg_3:
        return arg_2 + arg_3
    elif arg_1 > arg_2 <= arg_3:
        return arg_1 + arg_3
    elif arg_1 >= arg_3 < arg_2:
        return arg_1 + arg_2

print(my_func(arg_1, arg_2, arg_3))