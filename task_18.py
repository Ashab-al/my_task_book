#найти максимальный элемент в массиве целых чисел


array = [2, 4, 6, 8, 10, 110] 
index = 0
max_number = 0

while index <= len(array) - 1:
    if array[index] > max_number:
        max_number = array[index]
    index += 1

print(max_number)

