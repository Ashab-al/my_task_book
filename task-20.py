#создать массив из 10 целых случайных чисел

import random

array = []
max_size = 10

while len(array) != max_size:
    array = array + [int(random.random() * 100000)]
    
print(array)