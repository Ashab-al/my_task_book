# 9. вывести положительные четные элементы

array = [1, -2, 3, 4, 5, 6, 7, -8]
index = 0

while index <= len(array) - 1:
    if array[index] >= 0 and array[index] % 2 == 0: 
        print(array[index])
    index += 1