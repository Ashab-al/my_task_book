# найти дисперсию положительных элементов массива
'''
Формула для вычисления дисперсии выборки выглядит следующим образом:

[ s^2 =  frac{1}{n-1}  sum_{i=1}^{n} (x_i –  bar{x})^2 ]

Где:

( s^2 ) — дисперсия выборки
( n ) — количество значений в выборке
( x_i ) — каждое отдельное значение в выборке
(  bar{x} ) — среднее значение выборки
https://sky.pro/wiki/profession/kak-vychislit-dispersiyu-vyborki/
'''

array = [2, 4, -6, 8, 10]
deviations_sum = 0
index = 0
sum_positive_items = 0
quantity_positive_items = 0
while index <= len(array) - 1:
    if array[index] > 0:
        sum_positive_items += array[index]
        quantity_positive_items += 1
    index += 1

index = 0
average_value = sum_positive_items / quantity_positive_items

while index <= len(array) - 1:
    if array[index] > 0:
        deviations_sum = deviations_sum + (array[index] - average_value)**2
    index += 1
dispersion = deviations_sum / (quantity_positive_items - 1)
print(dispersion) # 13.333333333333334