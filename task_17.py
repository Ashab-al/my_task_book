# создать массив из 5 объектов класса из предыдущего задания. 
# Для последнего заполнить открытые поля значениями.

class Car:
    def __init__(self, number_of_wheels, color, horsepowers):
        self.__number_of_wheels = number_of_wheels
        self.color = color
        self.horsepowers = horsepowers
    
    @property
    def number_of_wheels(self):
        return self.__number_of_wheels
    
    @number_of_wheels.setter
    def number_of_wheels(self, new_number_of_wheels):
        if new_number_of_wheels > 0:
            self.__number_of_wheels = new_number_of_wheels
        return self.__number_of_wheels


cars = [Car(2, 'white', 300), Car(3, 'black', 100), Car(4, 'white', 400), Car(4, 'black', 600), Car(4, 'white', 520)]

cars[len(cars) - 1].horsepowers = 999
cars[len(cars) - 1].color = 'green'
