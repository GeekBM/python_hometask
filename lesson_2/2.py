a = int(input('Введите количество элементов списка '))
my_list = [input('Введите первый элемент списка ')]
i = 1
while 1 <= i < a:
    i = i + 1
    b = input('Введите следующий элемент списка ')
    print(my_list.append(b))
print(my_list)
my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
print(my_list)
