with open ('test_1.txt', 'w') as file:
    input_line = input('Enter text :\n')
    while input_line:
        file.write(f'{input_line}\n')
        input_line = input('Enter text :\n')
