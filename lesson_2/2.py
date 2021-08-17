a = int(input('Enter 1st number '))
b = str(input( 'Enter 1st word '))
c = int(input('Enter 2nd number '))
d = str(input('Enter 2nd word '))
list = [a, b, c, d]
print(list)
list[0], list[1] = list[1], list[0]
list[2], list[3] = list[3], list[2]
print(list)
