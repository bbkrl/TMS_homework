from functools import reduce


def check_is_A(word: str) -> str:
    """Make word in uppercase"""
    return word[0].lower() == 'a'


def map_example_1():
    """Пример кода с использованием map"""

    fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

    filter_object = map(lambda word: word.upper(), 5)

    print(filter_object)

    print(tuple(filter_object))


def filter_example_1():
    fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
    filter_object = filter(check_is_A, fruit)
    print(list(filter_object))


def filter_example_2():
    input_value = 'Артем'

    fruit = {'Глеб': 'Серафим', 'Артем': 'Веселко'}

    filter_object = filter(lambda x: x[0] == input_value, fruit.items())

    print(dict(filter_object))


def reduce_example_1():
    numbers = [0, 1, 2, 3, 4]

    result = reduce(lambda x, y: x + y, numbers)

    print(result)
    # 0 + 1 = 1
    # 1 + 2 = 3
    # 3 + 3 = 6
    # 6 + 4 = 10

    # 10


def reduce_example_2():
    numbers = [0, 1, 2, 3, 4]

    result = reduce(lambda x, y: x + y, numbers, 100)
    print(result)
    # 100 + 0 = 100
    # 100 + 1 = 101
    # 101 + 2 = 103
    # 103 + 3 = 106
    # 106 + 4 = 110
    # 110


def reduce_example_3():
    multipliers = [2, 10, 4, 16]

    accumulation = reduce(
        lambda acc, number: acc + number,
        multipliers,
    )
    print(accumulation)
    # 32


def reduce_example_4():
    values = [22, 4, 12, 43, 19, 71, 20]

    count = reduce(
        lambda x, y: x if y % 2 else x + 1,
        values,
        # 5 # Initializer
    )
    print(count)


if __name__ == '__main__':
    filter_example_1()

