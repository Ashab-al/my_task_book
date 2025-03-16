#7. сдвинуть элементы на заданное количество позиций без переноса (пустые места заполнять нулями)

array = [1, 2, 3, 4, 5]
max_shifts = 2
current_shift = 1

# while max_shifts >= current_shift:
#     index = -1
#     while index >= -(len(array))+1:
#         array[index] = array[index-1]
#         index -= 1
#     array[current_shift - 1] = 0
#     current_shift += 1
    
# print(array)

#[0, 0, 1, 2, 3]

# while max_shifts >= current_shift:
#     index = -1
#     while index >= -(len(array))+1:
#         array[index] = array[index-1]
#         index -= 1
#     array[current_shift - 1] = 0
#     current_shift += 1

array = [1, 2, 3, 4, 5]
max_shifts = 2
current_shift = 1

index = len(array) - 1
while max_shifts >= current_shift:
    array[index] = array[index-1]
    index -= 1
    if index == 0:
        array[current_shift - 1] = 0
        current_shift += 1
        index = len(array) - 1


print(array)