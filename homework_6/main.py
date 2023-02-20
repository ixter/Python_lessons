import menu  # менюшка
from random import randint

def task_1():
    print(
        'Задача 30: Заполните массив элементами арифметической прогрессии.\n'
        'Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.\n'
        'Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.\n'
        'Каждое число вводится с новой строки.\n'
        'Ввод: 7 2 5\n'
        'Вывод: 7 9 11 13 15\n'
    )
    number_one = enter_numbers('Первый элемент')
    number_two = enter_numbers('Разность элементов')
    number_three = enter_numbers('Количество элементов')

    solution_task_1(number_one, number_two, number_three)


def task_2():
    print('Задача 32: Определить индексы элементов массива (списка),\n'
          'значения которых принадлежат заданному диапазону\n'
          '(т.е. не меньше заданного минимума и не больше заданного максимума)\n'
          'Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]\n'
          'Вывод: [1, 9, 13, 14, 19]\n'
          )
    number_one = enter_numbers('Длинна списка')
    number_two = enter_numbers('MIN значение')
    number_three = enter_numbers('MAX значение')
    solution_task_2(number_one, number_two, number_three)


if __name__ == "__main__":
    menu.start_menu()


def enter_numbers(text: str, output_type=True) -> int | str:
    """
    Функция ввода значения
    :param text: текст для вывода
    :param output_type: True(число) or False(строка)
    :return: default int value, or string value
    """
    value = 0
    try:
        if output_type:
            value = int(input(text + ': '))
        else:
            value = input(text + ': ')
    except:
        print('Ошибка введен текст\n')
    return value


def solution_task_1(val_one: int, val_two: int, val_three: int):
    """
    Функция решения первой задачи
    :param val_one: int
    :param val_two: int
    :param val_three: int
    """
    lst = []
    for i in range(val_three):
        if i == 0:
            lst.append(val_one)
        else:
            lst.append(lst[i - 1] + val_two)
    print(lst)


def solution_task_2(val_one: int, val_two: int, val_three: int):
    """
    Функция решения второй задачи
    :param val_one: int
    :param val_two: int
    :param val_three: int
    """
    lst = [randint(-10, 10) for i in range(val_one)]
    print(lst)
    print(list(i for i in range(len(lst)) if val_two <= lst[i] <= val_three))