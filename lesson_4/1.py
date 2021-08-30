from sys import argv
script_name, first_param, second_param, third_param = argv
a = int(argv[1]) * int(argv[2]) + int(argv[3])
print("Имя скрипта: ", script_name)
print("Выработка в часах ", first_param)
print("Ставка в час ", second_param)
print("Премия: ", third_param)
print(f'Зарплата сотрудника составляет: {a}')
