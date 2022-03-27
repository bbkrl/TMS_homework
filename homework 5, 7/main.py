from functools import reduce


def decorator(func):
    """
    Функция-декоратор
    """

    print('декоратор')

    def wrapper():
        print('- старт программы...')
        print('-- до функции', func.__name__)
        func()
        print('-- после функции', func.__name__)
        print('- конец программы')

    return wrapper


def print_args_decorator(func):
    """
    Написать декоратор который выводит название декорируемой функции и ее аргументы
    """

    def wrapper(*args):
        print('Переданные аргументы и название функции: ')
        if not args:
            print('Функция не принимает никаких аргументов')
            print("название функции:", func.__name__)
        else:
            print(args, "название функции:", func.__name__, sep='\n')

    return wrapper


def countdown_decorator(sec):
    print('Таймер установлен на {} секунд'.format(sec))

    def my_decorator(func):
        import time

        def wrapper():
            for i in range(sec):
                my_time = sec - i
                m, s = divmod(my_time, 60)
                min_sec_format = '{:02d}:{:02d}'.format(m, s)
                print(min_sec_format, end='\n')
                time.sleep(1)
            print('Countdown finished.')
            func()

        return wrapper

    return my_decorator


def lambda_func():
    """
    Оставить в списке только четные числа
    """

    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_numbers = filter(lambda x: x % 2 == 0, list_numbers)
    for num in list_numbers:
        print(num, end=' ')


def wrapped():
    """
    Декорируемая функция
    """
    print('--- обернутая функция')


def rounding_to_a_whole():
    """
    Реализовать программу, которая принимает список из дробных чисел и округляет их до целого числа
    """
    values = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344, 32.00013]
    rounded_values = list(map(round, values))
    print(rounded_values)


def chek_more_eighty(num: int) -> bool:
    """
    проверка для функции more_than_eighty()
    """
    return num >= 80


def more_than_eighty():
    """
    Реализовать программу которая возвращает список из числе больше 80, на основе переданного списка
    """
    scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 92, 85]
    new_scores = list(filter(chek_more_eighty, scores))
    print(new_scores)


def check_is_palindromic(word: str) -> bool:
    """
    проверка для функции check_palindromic()
    :param word:
    :return:
    """
    return word == word[::-1]


def check_palindromic():
    """
    Реализовать программу которая ищет слова палиндромы из списка
    """

    values = ["demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP"]
    new_values = list(filter(check_is_palindromic, values))
    print(new_values)


def multiply():
    """
    Реализовать программу которая подсчитывает произведение чисел из списка
    :return:
    """

    values = [1, 2, 3, 4]
    result = reduce(lambda x, y: x * y, values)
    print(result)


def return_large_number():
    """
    Реализовать программу которая возвращает большее число из списка
    :return:
    """
    values = [3, 5, 101, 2, 4, 7, 1, 8, -1, 100]
    number = int(reduce(
        lambda x, y: x if x > y else y, values
    ))
    print(number)


def check(string):
    """
    функция в помощь для функции  number_of_words()
    """
    count = string.count('капитан')
    return count


def number_of_words():
    """
    Подсчитать количество слова капитан в списке
    """
    sentences = ['капитан джек воробей', 'капитан дальнего плавания', 'ваша лодка готова, капитан']
    number = len(list(map(check, sentences)))
    print(number)


if __name__ == "__main__":
    number_of_words()
