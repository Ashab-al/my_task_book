#сколько элементов больше минимального на 5?


array = [15, 10, 12, 17, 25, 30] 
index = 1
min_number = array[index - 1]
count = 0
current_number = 0

while index <= len(array) - 1:
    if array[index] < min_number:
        min_number = array[index]
        current_number = array[index - 1]
    else:
        current_number = array[index] 
    if current_number - min_number >= 5:
        count += 1

    index += 1

print(count) # 4

