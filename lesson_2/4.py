list = str(input('Введите несколько слов, разделенных пробелом: '))
list = list.split(' ')
for num, elem in enumerate (list, 1):
    print(f'#{num} - {elem[:10]}')
