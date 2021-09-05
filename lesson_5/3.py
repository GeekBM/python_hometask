with open('test_3.txt') as file:
    file_lines = file.readlines()
    emp = {}
    sal = 0
    for i in file_lines:
        emp_info = i.split()
        emp.update({emp_info[0]: float(emp_info[1])})
        sal += float(emp_info[1])
av_sal = sal / len(emp)
print(f'Avarage = {av_sal}')
for k, v in emp.items():
    if v < 20000:
        print(f'{k}: {v}')
