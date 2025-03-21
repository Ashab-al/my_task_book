#сколько элементов больше минимального на 5?

array = [15, 20, 12, 17, 25, 10]
index = 0
min_number = array[index]
minimum_element_found = False
count = 0

while index <= len(array) - 1:
    if array[index] < min_number and minimum_element_found == False:
        min_number = array[index]
    
    index += 1

    if index > len(array) - 1 and minimum_element_found == False:
        minimum_element_found = True
        index = 0
    
    if index <= len(array) - 1 and minimum_element_found and array[index] - min_number == 5:
        count += 1
        print(array[index]) # 15
        
    

print(min_number) # 10
print(count) # 1

