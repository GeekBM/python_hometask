file = open('test_1.txt', 'w')
line = input('Введите текст \n')
while line:
    file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

file.close()
file = open('test_1.txt', 'r')
content = file.readlines()
print(content)
file.close()
