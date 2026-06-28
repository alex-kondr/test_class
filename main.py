# class Animal:
#     color = "Black"
#     len_animal = 10

#     def set_color(self, color: str):
#         self.color = color

#     def set_food(self, food):
#         print(f"Годуємо тварину за допомогою {food}...")


# cow_1 = Animal()
# cow_1.set_color("White")
# cow_1.speed = 100
# print(cow_1.speed)

# cow_2 = Animal()
# print(cow_2.speed)

# cow_3 = Animal()
# cow_4 = Animal()
# cow_5 = Animal()


# class Vehicle:
#     fuel = "gas"
#     _protect_attr = "protected"
#     __private_attr = "private"

#     def __init__(self, color: str, brand: str):
#         self.color = color
#         self.brand = brand

#     def move(self):
#         print("Транспорт рухається")

#     def _stop(self):
#         print("Stoped")

#     def chage_protect_level(self, name: str):
#         self._protect_attr = name

#     def __change_fuel(self, name: str):
#         self.fuel = name

# BMW = Vehicle("Black", "BMW")
# BMW.move()
# print(BMW._protect_attr)
# BMW._stop()

# print(BMW.__private_attr)
# print(BMW._Vehicle__private_attr)
# BMW._Vehicle__change_fuel("disel")
# print(BMW.fuel)

# print(BMW.color)
# print(BMW.brand)


# 1. Створити клас BankAccount, який матиме публічний
# атрибут account_holder, захищений атрибут _balance
# та приватний атрибут __pin_code.change_weight
# 2. Забезпечити можливість взаємодії з
# балансом через публічні методи, не дозволяючи змінювати баланс напряму.
# 3. Використати захищений метод для перевірки балансу.
# 4. Забезпечити приватний метод для оновлення PIN-коду.


# from typing import Any


# class BankAccount:
#     account_holder = "user"
#     _balance = 0
#     __pin_code = 4561

#     def add_cash(self, count: float|int):
#         self._balance += count

#     def buy(self, count: float|int):
#         if self._balance > 0 and count <= self._balance:
#             self._balance -= count

#     def _check_balance(self):
#         return self._balance

#     def __change_pin_code(self, new_pin):
#         self.__pin_code = new_pin


# class MyClass:
#     def __init__(self, name, number: int = 0):
#         self.name = name
#         self.number = number

#     def __len__(self) -> int:
#         return len(self.name)

#     def __gt__(self, other: "MyClass"):
#         return self.number > other.number

#     def __le__(self, other: "MyClass"):
#         return len(self.name) <= len(other.name)

#     def __call__(self, *args: Any, **kwargs: Any) -> Any:
#         print(f"'{args=}'\n'{kwargs=}'")

#     def __add__(self, other: "MyClass"):
#         return self.number + other.number

#     def __sub__(self, other):
#         return self.number - other.number

#     def __mul__(self, other):
#         return self.number * other.number

#     def __pow__(self, other):
#         return self.number ** other.number

#     def __str__(self) -> str:
#         return f"My name '{self.name}'"


# name = "Alex"
# print(len(name))

# obj_1 = MyClass("NameName", 10)
# print(len(obj))
# obj_2 = MyClass("Other", 5)
# print(obj_1 <= obj_2)
# obj_1("Name", "Color", brand="Toyota", fuel="disel")
# print(obj_1 ** obj_2)
# print(obj_1)


class Animal:
    eat = False
    weight = 20

    def run(self):
        self.eat = False
        print("Тварина біжить...")

    def sleep(self):
        self.eat = False
        print("Тварина спить...")

    def eating(self):
        self.eat = True
        print("Тварина їсть...")

    def left(self):
        print("Тварина повертає на ліво")


class Head:
    def left(self):
        print("Повертаєм голову на ліво")

    def down(self):
        print("Повертаємо голову вниз")


class Cow(Animal):
    color="White"

    def __init__(self, weight):
        self.weight = weight


class Paw(Head, Animal):
    def __init__(self, color):
        self.color = color

    def run(self):
        if not self.eat:
            print("Собака не може бігти голодна")
        else:
            super().run()


class WhitePaw(Paw):
    def __init__(self):
        self.color = "White"


# cow_1 = Cow(weight=250)
# print(f"Вага корови: {cow_1.weight}")

# paw_1 = Paw(color="Black")
# # print(f"Колір песика: {paw_1.color}")
# paw_1.eating()
# paw_1.run()
# print(paw_1.eat)
# paw_1.run()


# class Book:
#     def __init__(self, count: int, author: str, name: str):
#         self.count = count
#         self.author = author
#         self.name = name

#     def __str__(self):
#         return f"Name: {self.name}/{self.count} - Author: {self.author}"


# book_1 = Book(400, "Author-1", "Book-1")
# print(book_1)


from typing import Optional, List, Union


class Author:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: Optional[int]=None,
        country: Optional[str]=None
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.age}"

    def change_age(self, age: int):
        if age > 0:
            self.age = age
            print("Вік успішно змінено")
        else:
            print("Вік не може бути від'ємним")

    def set_country(self, country: str):
        self.country = country


class Title:
    def __init__(self, title: str, style: Optional[str]=None, subtitle: Optional[str]=None):
        self.title = title
        self.subtitle = subtitle
        self.style = style


class Book:
    def __init__(self, count: int, title: Title):
        self.count = count
        self.authors: List[Author] = []
        self.title = title

    def __str__(self):
        return f"Name: {self.title.title}/{self.count} - Authors: {self.authors}"


author_1 = Author("Alex", "Kondr", 19)
# book_1 = Book(count=125, author=author_1, name="Book-1")
# print(book_1)
author_1.change_age(26)
print("Before...")
print(author_1.country)
# print(author_1.age)
# print(book_1.author.age)
book_1.author.change_country("Odesa")
print("After...")
print(author_1.country)

