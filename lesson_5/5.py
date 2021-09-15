with open ('test_5.txt') as file:
    nums_str = file.read().split()
    sum = 0
    for num in nums_str:
        sum += int(num)

print(sum)
