#11. найти среднее арифметическое элементов массива

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
sum = 0

while index <= len(array) - 1:
    sum += array[index]
    index += 1
print(sum / len(array))
# 5.5