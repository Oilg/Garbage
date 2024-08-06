from abc import ABC, abstractmethod


class ICharacteristics(ABC):

    @abstractmethod
    def horse_power(self):
        raise NotImplementedError

    @abstractmethod
    def speed(self):
        raise NotImplementedError


class Car:

    @property
    def color(self) -> str:
        return "red"

    @color.setter
    def color(self, value: str) -> None:
        self.color = value

Car.color

class Car(ICharacteristics, ABC):

    def __init__(self):
        self.__horse_power = ''
        self.__speed = ''

    @property.fget
    def get_horse_power(self):
        return self.__horse_power

    @property.fdel
    def del_horse_power(self):
        del self.__horse_power

    def speed(self):
        return "Speed = "

    def turn_left(self):  # убрать в интерфейс
        raise NotImplementedError

    def turn_right(self):  # убрать в интерфейс
        raise NotImplementedError

    @staticmethod
    def available_colors():
        return ["black", "blue", "gray"]


Car.available_colors()


class ICarBodyForm(ABC):
    @abstractmethod
    def form(self):
        raise NotImplementedError


class Sedan(Car, ICarBodyForm):
    def horse_power(self):
        print(Car.horse_power(self) + "180 for sedan")

    def speed(self):
        print(Car.speed(self) + "120 for sedan")

    def turn_left(self):
        print("Turning steering wheel to left the car will go to the left")

    def turn_right(self):
        print("ololo")

    def form(self):
        print("Form: long with 5 doors")


print("Это седан")
sedan = Sedan()
sedan.horse_power()
sedan.speed()
sedan.turn_left()
sedan.form()


class Hatchback(Car, ICarBodyForm):
    def horse_power(self):
        print(Car.horse_power(self) + "200 for sedan")

    def speed(self):
        print(Car.speed(self) + "220 for sedan")

    def turn_left(self):
        print("Turning steering wheel to left the car will go to the left")

    def turn_right(self):
        print("Turning steering wheel to right the car will go to the right")

    def form(self):
        print("Form: short with 3 doors")


print("Это хечбэк")
hatchback = Hatchback()
hatchback.horse_power()
hatchback.speed()
hatchback.turn_right()
hatchback.form()

# TODO посмотреть что такое @property, @class_method, @static_method
# TODO посмотреть что такое generic

# класс VolvoCar c дженериками на седан и хетчбэк
class VolvoCarSedan(Sedan):
    ...


class VolvoCarHatchback(Hatchback):
    ...

print("Это вольво седан")
volvo_sedan = VolvoCarSedan()
volvo_sedan.speed()
volvo_sedan.form()
print("Это вольво хечбэк")
volvo_hatchback = VolvoCarHatchback()
volvo_hatchback.speed()
volvo_hatchback.form()


a = {[3, 4]: 147}
a([3, 4])