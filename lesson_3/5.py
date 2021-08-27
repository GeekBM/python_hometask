def my_sum():
    sum_res = 0
    z = False
    while z is False:
        nums = input('Введите числа или "z", чтобы закончить ').split()
        res = 0
        for elem in range(len(nums)):
            if nums[elem] == "z":
                z = True
                break
            else:
                res += int(nums[elem])
        sum_res += res
        print(f"Последняя сумма - {sum_res}")
    print(f'Общая сумма - {sum_res}')


my_sum()
