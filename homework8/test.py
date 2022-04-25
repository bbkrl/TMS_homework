class Wheel:
    """
    Wheel (колесо), который принимает в себя диаметр (16-21, необходимо сделать проверку на вхождение в этот
    диапазон) и вес колеса в кг. Этот класс методов не имеет
    """

    def __init__(self, wheel_weight, wheel_diameter):
        self.wheel_weight = wheel_weight
        self.wheel_diameter = wheel_diameter

        try:
            self.wheel_diameter in range(16, 22)
        except Exception as e:
            print(e)
            # self.wheel_diameter = 19


a = Wheel(21, 13)
print(a)

