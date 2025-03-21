#найти максимальный элемент в массиве целых чисел


array = [-2, -4, -6, -8, -10, -110] 
i = 0
max_number = array[i]

while i <= len(array) - 1:
    if array[i] > max_number:
        max_number = array[i]
    i += 1

print(max_number) # -2 а если все числа будут положительными, то выведет 110

