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
# та приватний атрибут __pin_code.
# 2. Забезпечити можливість взаємодії з
# балансом через публічні методи, не дозволяючи змінювати баланс напряму.
# 3. Використати захищений метод для перевірки балансу.
# 4. Забезпечити приватний метод для оновлення PIN-коду.


from typing import Any


class BankAccount:
    account_holder = "user"
    _balance = 0
    __pin_code = 4561

    def add_cash(self, count: float|int):
        self._balance += count

    def buy(self, count: float|int):
        if self._balance > 0 and count <= self._balance:
            self._balance -= count

    def _check_balance(self):
        return self._balance

    def __change_pin_code(self, new_pin):
        self.__pin_code = new_pin


class MyClass:
    def __init__(self, name, number: int = 0):
        self.name = name
        self.number = number

    def __len__(self) -> int:
        return len(self.name)

    def __gt__(self, other: "MyClass"):
        return self.number > other.number

    def __le__(self, other: "MyClass"):
        return len(self.name) <= len(other.name)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print(f"'{args=}'\n'{kwargs=}'")

    def __add__(self, other: "MyClass"):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __pow__(self, other):
        return self.number ** other.number

    def __str__(self) -> str:
        return f"My name '{self.name}'"


# name = "Alex"
# print(len(name))

obj_1 = MyClass("NameName", 10)
# print(len(obj))
obj_2 = MyClass("Other", 5)
# print(obj_1 <= obj_2)
# obj_1("Name", "Color", brand="Toyota", fuel="disel")
# print(obj_1 ** obj_2)
print(obj_1)