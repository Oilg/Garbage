from abc import ABC, abstractmethod


class ICharacteristics(ABC):

    @abstractmethod
    def horse_power(self):
        raise NotImplementedError

    @abstractmethod
    def speed(self):
        raise NotImplementedError


class Car(ICharacteristics, ABC):

    def horse_power(self):
        return "Horse power = "

    def speed(self):
        return "Speed = "

    def turn_left(self):  # убрать в интерфейс
        raise NotImplementedError

    def turn_right(self):  # убрать в интерфейс
        raise NotImplementedError


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
