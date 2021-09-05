with open ('test_2.txt') as file:
    file_lines = file.readlines()
    for num, line in enumerate(file_lines):
        words_count = len(line.split())
        print(f'№ {num + 1} - {words_count} words')
