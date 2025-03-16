array = [7, 8, 9, 10, 11, 12, 13]
number_of_shifts = 3
current_number_of_shift = 1

while number_of_shifts >= current_number_of_shift:
    array.pop()
    array = [0] + array
    current_number_of_shift += 1

print(array)
