# 13. есть ли в массиве четные положительные элементы?

array = [-2, -4, -6, 8, 10] 
index = 0

while index <= len(array):
    if array[index] > 0 and array[index] % 2 == 0:
        print(array[index])
        break
    index += 1

