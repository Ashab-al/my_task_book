#8. поменять местами элементы в каждой паре

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0

while index <= len(array) - 1 and len(array) % 2 == 0:
    first_item = array[index]
    array[index] = array[index + 1]
    array[index + 1] = first_item
    
    index += 2

print(array)