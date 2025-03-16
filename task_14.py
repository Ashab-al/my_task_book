"""
14. какое максимальное количество подряд идущих элементов находится в массиве? 
0, 1, 3, 6, 7, 8 - в этом массиве подряд идут 0, 1 и 6, 7, 8. Максимальное количество - 3.
"""

array = [0, 1, 3, 6, 7, 8]

max_size = 0

counter = 0
index = 0

while index <= len(array) - 1:
    if index != 0 and array[index - 1] + 1 == array[index]:
        counter += 1
    else:
        counter = 1        
    if counter > max_size:
        max_size = counter
    index += 1
    
print(max_size)
