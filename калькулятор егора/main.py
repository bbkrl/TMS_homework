# def calculator(*args, **kwargs):
#     next == input('Нажмите любую клавишу для продолжения')
#     while next == 'Нажмите любую клавишу для продолжения':
#     if operation == '+':
#          print(f_number + s_number)
#     elif operation == '-':
#     print(f_number - s_number)
#     elif operation == '*':
#     print(f_number * s_number)
#     elif operation == '/':
#     print(f_number / s_number)
#     elif operation == '**':
#     print(f_number ** s_number)
#     else:
#     print('Error')
#
#
# if __name__ == '__main__':
#     f_number = float(input('Ведите первое число'))
#     operation = input('Введите операцию')
#     s_number = float(input('Введите второе число'))
#     calculator(f_number, s_number, operation="+")

def calc(operation: str, f_number: int, s_number: int):
    while True:
        if operation == '+':
            return f_number + s_number
        elif operation == '-':
            return f_number - s_number
        elif operation == '*':
            return f_number * s_number
        elif operation == '/':
            return f_number / s_number
        elif operation == '**':
            return f_number ** s_number


def calc_in_console():
    while True:
        f_number = float(input('Ведите первое число'))
        operation = input('Введите операцию')
        s_number = float(input('Введите второе число'))
        if operation == '+':
            print(f_number + s_number)
        elif operation == '-':
            print(f_number - s_number)
        elif operation == '*':
            print(f_number * s_number)
        elif operation == '/':
            print(f_number / s_number)
        elif operation == '**':
            print(f_number ** s_number)
        key = input("Press q to extit, or smth to continue")
        if key == "q":
            exit(0)


if __name__ == "__main__":
    # print(calc("+", 12, 22))
    calc_in_console()
