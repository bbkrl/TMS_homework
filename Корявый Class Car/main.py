from tkinter import N
from tkinter.messagebox import NO


class Engine:
    """
    Класс Engine (мотор), который будет принимать в себя тип мотора(v6, v8, v10), каждый из этих типов имеет коэффициент
    разгона: v6-0.2, v8-0.4, v10-0.6, лошадиные силы (любое значение), флаг отображающий присутствие турбины (True,
    False) добавляющий дополнительный коэффициент разгона равный 0.8. Этот класс имеет один метод generate_power,
    который возвращает мощность вырабатываемой мотором, по формуле: Лошадиные силы * коэффициент разгона мотора /
    коэффициент разгона от турбины (если он есть)

    """

    def __init__(self, horse_power: int, turbine: bool):
        self.type_of_engines = {
            "engine_type_v6": 0.2,
            "engine_type_v8": 0.4,
            "engine_type_v10": 0.6
        }

        self.horse_power = horse_power
        self.__turbine = turbine
        self.__turbine_coefficient = 0.8

    def generate_power(self, k_type_of_engine):
        if self.__turbine:
            engine_power = (self.horse_power * self.type_of_engines[k_type_of_engine]) / self.__turbine_coefficient
        else:
            engine_power = (self.horse_power * self.type_of_engines[k_type_of_engine])
        return engine_power


class Wheel:
    """
    Wheel (колесо), который принимает в себя диаметр (16-21, необходимо сделать проверку на вхождение в этот
    диапазон) и вес колеса в кг. Этот класс методов не имеет
    """

    def __init__(self, wheel_weight, wheel_diameter):
        self.wheel_weight = wheel_weight
        self.wheel_diameter = wheel_diameter
        # try:
        #     wheel_diameter in range(16, 21+1)
        # except Exception as e:
        #     print('Wrong diametr', e)


class Car(Engine, Wheel):
    """Car (машина), который принимает в себя объект мотора, массив из объектов колес, если передано меньше 4 –
    выкидывать ошибку(почитайте о raise Exception) и тип машины: легковая, джип и грузовая, каждый из типов имеет свой
    вес в кг (легковая 1200, джип 1500,  грузовая 1800) Этот класс имеет следующие методы: start_engine,
    который заводит мотор move, который принимает в себя дистанцию на заезд в метрах и возвращает время в секундах за
    которое эту дистанцию проедет автомобиль. Логика вычисления следующая: 1. Если двигатель не заведен - выкидывать
    ошибку (почитайте о raise Exception) 2. Форму вычисления времени: (Вес автомобиля + вес колес) / мощность мотора (
    из метода generate_power) * длинна заезда
    """

    def __init__(self, horse_power: int, turbine: bool, wheel_weight: int, wheel_diameter: int,
                 num_of_wheel: int):
        Engine.__init__(self, horse_power, turbine)
        Wheel.__init__(self, wheel_weight, wheel_diameter)
        self.num_of_wheel = num_of_wheel
        self.type_of_car = {
            'passenger': 1200,
            'truck': 1800,
            'jeep': 1500
        }

    def engine_start_func(self, start_engine_key: bool):
        if not start_engine_key:
            raise Exception("Двигатель не запущен!")

    def move(self, key: bool, distance: int, type_of_car_key, k_type_of_power) -> float:
        self.engine_start_func(key)
        move_time = ((self.wheel_weight * self.num_of_wheel + self.type_of_car[
            type_of_car_key]) * distance) / self.generate_power(k_type_of_power)
        return move_time


if __name__ == '__main__':
    a = Car(12300, False, 20, 21, 4)
    car = Car(1000, True, 25, 100, 10)
