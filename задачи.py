#1
class Student:
    def init(self, name, age, average_grade):
        self.name = name
        self.age = age
        self.average_grade = average_grade

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_average_grade(self):
        return self.average_grade

    def set_average_grade(self, average_grade):
        self.average_grade = average_grade




Создание объекта класса "Студент"
student = Student("Иванов", 20, 4.5)

 Получение значения поля "имя"
print("Имя студента:", student.get_name())

 Установка нового значения поля "имя"
student.set_name("Петров")

 Получение значения поля "возраст"
print("Возраст студента:", student.get_age())

 Установка нового значения поля "возраст"
student.set_age(21)

 Получение значения поля "средний балл"
print("Средний балл студента:", student.get_average_grade())

 Установка нового значения поля "средний балл"
student.set_average_grade(4.8)

#2
class Rectangle:
    def init(self, length, width):
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


 Создание объекта класса "Прямоугольник"
rectangle = Rectangle(5, 3)

 Получение значения поля "длина"
print("Длина прямоугольника:", rectangle.get_length())

 Установка нового значения поля "длина"
rectangle.set_length(7)

 Получение значения поля "ширина"
print("Ширина прямоугольника:", rectangle.get_width())

 Установка нового значения поля "ширина"
rectangle.set_width(4)

 Вычисление площади
print("Площадь прямоугольника:", rectangle.calculate_area())

 Вычисление периметра
print("Периметр прямоугольника:", rectangle.calculate_perimeter())

#3
class Car:
    def init(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def set_brand(self, brand):
        self.brand = brand

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_mileage(self, mileage):
        self.mileage = mileage

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage


 Создание объекта класса "Автомобиль"
car = Car("mersedes", "BMW", 2020, 50000)

 Вывод значений атрибутов
print("Марка:", car.get_brand())
print("Модель:", car.get_model())
print("Год выпуска:", car.get_year())
print("Пробег:", car.get_mileage())

 Изменение значений атрибутов
car.set_brand("Honda")
car.set_model("Accord")
car.set_year(2018)
car.set_mileage(60000)

 Вывод обновленных значений атрибутов
print("Марка:", car.get_brand())
print("Модель:", car.get_model())
print("Год выпуска:", car.get_year())
print("Пробег:", car.get_mileage())


#4

class BankAccount:
    def __init__(self, client_name, initial_balance=0):
        self.client_name = client_name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств на счете.")

    def get_balance(self):
        return self.balance



 Создание объекта класса "Банковский счет"
account = BankAccount("Иванов", 1000)

 Вывод текущего баланса счета
print("Текущий баланс счета:", account.get_balance())

 Пополнение счета на 500
account.deposit(500)

 Вывод обновленного баланса счета
print("Обновленный баланс счета:", account.get_balance())

 Снятие 1500 со счета
account.withdraw(1500)

 Вывод обновленного баланса счета
print("Обновленный баланс счета:", account.get_balance())




class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def set_brand(self, brand):
        self.brand = brand

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_mileage(self, mileage):
        self.mileage = mileage

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage


