class Engine:
    """
    Класс Engine (мотор), который будет принимать в себя тип мотора(v6, v8, v10), каждый из этих типов имеет коэффициент
    разгона: v6-0.2, v8-0.4, v10-0.6, лошадиные силы (любое значение), флаг отображающий присутствие турбины (True,
    False) добавляющий дополнительный коэффициент разгона равный 0.8. Этот класс имеет один метод generate_power,
    который возвращает мощность вырабатываемой мотором, по формуле: Лошадиные силы * коэффициент разгона мотора /
    коэффициент разгона от турбины (если он есть)

    """

    def __init__(self, horse_power: int, turbine: bool):
        # self.engine_type = engine_type
        self.horse_power = horse_power
        self.__turbine = turbine
        self.__engine_type_v6 = 0.2
        self.__engine_type_v8 = 0.4
        self.__engine_type_v10 = 0.6
        self.__turbine_coefficient = 0.8

    def generate_power(self):
        if self.__turbine:
            engine_power = (self.horse_power * self.__engine_type_v10) / self.__turbine_coefficient
        else:
            engine_power = (self.horse_power * self.__engine_type_v6)
        return engine_power


class Wheel:
    """
    Wheel (колесо), который принимает в себя диаметр (16-21, необходимо сделать проверку на вхождение в этот
    диапазон) и вес колеса в кг. Этот класс методов не имеет
    """

    def __init__(self, wheel_weight, wheel_diameter):
        self.wheel_weight = wheel_weight
        self.wheel_diameter = wheel_diameter


class Car(Engine, Wheel):
    """Car (машина), который принимает в себя объект мотора, массив из объектов колес, если передано меньше 4 –
    выкидывать ошибку(почитайте о raise Exception) и тип машины: легковая, джип и грузовая, каждый из типов имеет свой
    вес в кг (легковая 1200, джип 1500,  грузовая 1800) Этот класс имеет следующие методы: start_engine,
    который заводит мотор move, который принимает в себя дистанцию на заезд в метрах и возвращает время в секундах за
    которое эту дистанцию проедет автомобиль. Логика вычисления следующая: 1.	Если двигатель не заведен - выкидывать
    ошибку (почитайте о raise Exception) 2.	Форму вычисления времени: (Вес автомобиля + вес колес) / мощность мотора (
    из метода generate_power) * длинна заезда
    """

    def __init__(self, horse_power: int, turbine: bool, wheel_weight: int, wheel_diameter: int, num_of_wheel: int):
        Engine.__init__(self, horse_power, turbine)
        Wheel.__init__(self, wheel_weight, wheel_diameter)
        self.num_of_wheel = num_of_wheel
        self.__passenger = 1200
        self.__truck = 1800
        self.__jeep = 1500

    def start_engine(self, key: int) -> bool:
        if key:
            engine_running = True
            print('Двигатель запущен')
            return engine_running

        else:
            engine_running = False
            print('Двигатель выключен')
            return engine_running

    def move(self, distance: int) -> float:
        if not Car.start_engine:
            raise Exception("Двигатель не запущен!")
        move_time = ((self.wheel_weight * self.num_of_wheel + self.__jeep) * distance) / self.generate_power()
        return move_time


car1 = Car(639, False, 20, 19, 4)
car1.start_engine(0)
print(car1.move(100))
