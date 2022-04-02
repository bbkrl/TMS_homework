class Engine:
    """
    Класс Engine (мотор), который будет принимать в себя тип мотора(v6, v8, v10), каждый из этих типов имеет коэффициент
    разгона: v6-0.2, v8-0.4, v10-0.6, лошадиные силы (любое значение), флаг отображающий присутствие турбины (True,
    False) добавляющий дополнительный коэффициент разгона равный 0.8. Этот класс имеет один метод generate_power,
    который возвращает мощность вырабатываемой мотором, по формуле: Лошадиные силы * коэффициент разгона мотора /
    коэффициент разгона от турбины (если он есть)

    """
    motor_type_v6 = 0.2
    __motor_type_v8 = 0.4
    __motor_type_v10 = 0.6
    __turbine_coefficient = 0.8

    def __init__(self, engine_type, horse_power: int, turbine=False):
        self.engine_type = engine_type
        self.horse_power = horse_power
        self.turbine = turbine

    def generate_power(self):
        if self.turbine:
            engine_power = (self.horse_power * self.engine_type) / 0.8
        else:
            engine_power = (self.horse_power * self.engine_type)
        return engine_power


if __name__ == "__name__":
    print(1111)
    engine1 = Engine(0.2, 639, False)
    print(type(engine1))