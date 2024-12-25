from abc import ABC, abstractmethod

# Абстракция
class Animal(ABC):
    # Абстрактный метод, который должен быть реализован в дочерних классах
    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print(f"{self.class.name} спит.")

# Наследование и инкапсуляция
class Dog(Animal):
    def init(self, name, age):
        self.__name = name  # инкапсуляция
        self.__age = age    # инкапсуляция

    def make_sound(self):
        print(f"{self.__name} говорит: Гав!")

    def get_name(self):  # геттер
        return self.__name

    def set_name(self, name):  # сеттер
        self.__name = name

    def get_age(self):  # геттер
        return self.__age

    def set_age(self, age):  # сеттер
        if age > 0:
            self.__age = age
        else:
            print("Возраст должен быть положительным числом.")

# Наследование и инкапсуляция
class Cat(Animal):
    def init(self, name, age):
        self.__name = name  # инкапсуляция
        self.__age = age    # инкапсуляция

    def make_sound(self):
        print(f"{self.__name} говорит: Мяу!")

    def get_name(self):  # геттер
        return self.__name

    def set_name(self, name):  # сеттер
        self.__name = name

    def get_age(self):  # геттер
        return self.__age

    def set_age(self, age):  # сеттер
        if age > 0:
            self.__age = age
        else:
            print("Возраст должен быть положительным числом.")

# Полиморфизм
def animal_sound(animal):
    animal.make_sound()

# Создание объектов
dog = Dog("Рекс", 5)
cat = Cat("Барсик", 3)

# Демонстрация инкапсуляции через геттеры и сеттеры
print(dog.get_name())  # Рекс
dog.set_name("Макс")
print(dog.get_name())  # Макс

# Демонстрация полиморфизма
animal_sound(dog)  # Макс говорит: Гав!
animal_sound(cat)  # Барсик говорит: Мяу!

# Демонстрация абстракции
dog.sleep()  # Макс спит.
cat.sleep()  # Барсик спит.
