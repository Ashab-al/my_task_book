# 10. заполнить массив по формуле a[i] = i ^ 2 +10

array = [1, 2, 3 ,4 ,5, 6, 7, 8]
index = 0

while index <= len(array) - 1:
    array[index] = index ** 2 + 10

    index += 1

# [10, 11, 14, 19, 26, 35, 46, 59]