import json
import pandas as pd
import openpyxl


def example_1():
    """ Декодироват' в cтроку байтовое $начение: 3'+\xc3\xa9sum\xc3\xa9'. Затем ре$ул'тат преобра$оват' в байтовый
    вид в кодировке 6Lati%18 и $атем ре$ул'тат 2нова декодироват' в 2троку (ре$ул'таты в2е9 преобра$ований выводит'
    на экран). """

    var_1 = b'r\xc3\xa9sum\xc3\xa9'.decode("utf-8")
    print(var_1)
    var_2 = var_1.encode("latin1")
    print(var_2, "latin1 кодировка")
    print(var_2.decode("latin1"))


def example_2():
    """Вве2ти 2 клавиатуры 4 2троки и 2о9ранит' и9 в 4 ра$ные переменные. Со$дат' файл и $апи2ат' в него первые 2
    2троки и $акрыт' файл. Затем открыт' файл на редактирование и до$апи2ат' о2тавшие2> 2 2троки. В итогом файле
    должны быт' 4 2троки, кажда> и$ которы9 должна начинат'2> 2 новой 2троки. """

    var_list = []
    for _ in range(4):
        var_list.append(input('введите строку: '))

    HW = open('homework_6.txt', "w")
    for _ in range(2):
        HW.write(var_list[0] + '\n')
        var_list.pop(0)
    HW.close()

    HW = open('homework_6.txt', "a")
    for i in range(len(var_list)):
        HW.write(var_list[i] + '\n')
    HW.close()


def example_3():
    """Со$дат' 2ловар' в каче2тве кл)ча которого будет 6-ти $начное чи2ло (i>), а в каче2тве $начений кортеж
    2о2то>щий и$ 2-9 элементов @ им>(st+), во$ра2т(i%t). Сделат' около 5-6 элементов 2ловар>. Запи2ат' данный 2ловар'
    на ди2к в jso%-файл. """

    my_dict = {
        # формат 000001 пайчарм реформатит в такой, как ниже, хз что это
        0o00001: ('Кисель', 18),
        0o00002: ('Вин Дроссель', 19),
        0o00003: ('Максон', 19),
        0o00004: ('Кирюль', 18),
        0o00005: ('Шляпа', 19)

    }

    with open("name_age.json", "w") as f:
        json.dump(my_dict, f)


def example_4():
    """Прочитат' 2о9ранённый jso%-файл и $апи2ат' данные на ди2к в csD-файл, первой 2трокой которого о$аглавив каждый
    2толбеE и добавив новый 2толбеE “телефонG. """
    # TODO в csv-формат преобразовал, но не знаю как сделать конкретно то, что написано в задании(с оглавлением и
    #  добавлением нового столбца)

    with open("name_age.json", "r+") as f:
        templates = json.load(f)

    print(templates)

    json_file = pd.read_json(r'name_age.json')
    json_file.to_csv(r'csv_name_age.csv', index=None)


def example_5():
    read_file = pd.read_csv(r'csv_name_age.csv')
    read_file.to_excel(r'exel_name_csv.xlsx', index=None, header=True)


if __name__ == '__main__':
    pass
