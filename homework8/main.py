class Engine:
    """
    Класс Engine (мотор), который будет принимать в себя тип мотора(v6, v8, v10), каждый из этих типов имеет коэффициент
    разгона: v6-0.2, v8-0.4, v10-0.6, лошадиные силы (любое значение), флаг отображающий присутствие турбины (True,
    False) добавляющий дополнительный коэффициент разгона равный 0.8. Этот класс имеет один метод generate_power,
    который возвращает мощность вырабатываемой мотором, по формуле: Лошадиные силы * коэффициент разгона мотора /
    коэффициент разгона от турбины (если он есть)

    """
    __engine_type_v6 = 0.2
    __engine_type_v8 = 0.4
    __engine_type_v10 = 0.6
    __turbine_coefficient = 0.8

    def __init__(self, horse_power: int, engine_type=__engine_type_v10, turbine=False):  # TODO хз как сделать более
        # TODO норм выбор типа мотора
        self.__engine_type_v6 = engine_type
        self.horse_power = horse_power
        self.turbine = turbine

    def generate_power(self):
        if self.turbine:
            engine_power = (self.horse_power * self.__engine_type_v6) / self.__turbine_coefficient
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
        while True:
            self.wheel_diameter = wheel_diameter
            if 16 <= wheel_diameter <= 21:
                break
            else:
                print("Неподходящий диметр")
                continue






jz_2 = Engine(1000, turbine=True)
print(jz_2.generate_power())
