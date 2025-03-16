array = [0, 0, 0]

start_index = len(array) // 3
index = start_index

while start_index <= index <= start_index * 2 - 1:
    array[index] = 1
    index += 1

print(array)