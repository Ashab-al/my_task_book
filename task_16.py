"""
описать класс, у объекта которого будет 2 открытых поля и 1 скрытое с методами доступа. 
создать в основной программе 2 экземпляра этого класса
"""

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
        self.__number_of_wheels = new_number_of_wheels
        return self.__number_of_wheels

car_one = Car(4, 'black', 400)
car_one.number_of_wheels # 4
car_one.number_of_wheels = 5 # 5

car_second = Car(4, 'white', 500)

