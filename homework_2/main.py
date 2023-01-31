import menu  # менюшка
from random import randint
from math import sqrt


def task_1():
    print('Задача 10: На столе лежат n монеток.\n'
          'Некоторые из них лежат вверх решкой, а некоторые – гербом.\n'
          'Определите минимальное число монеток, которые нужно перевернуть,\n'
          'чтобы все монетки были повернуты вверх одной и той же стороной.\n'
          'Выведите минимальное количество монет, которые нужно перевернуть\n'
          '5 -> 1 0 1 1 0\n'
          '2\n')
    numbers = enter_numbers('Введите сколько монеток лежит на столе')
    solution_task_1(numbers)


def task_2():
    print('Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.\n'
          'Петя помогает Кате по математике.\n'
          'Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.\n'
          'Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.\n'
          'Помогите Кате отгадать задуманные Петей числа.\n'
          '4 4 -> 2 2\n'
          '5 6 -> 2 3\n')
    number_one = enter_numbers('Введите сумму чисел')
    number_two = enter_numbers('Введите произведение чисел')
    solution_task_2(number_one, number_two)


def task_3():
    print('Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.\n'
          '10 -> 1 2 4 8\n'
          'пользователь будет вводить каждое число на новой строке для задач 10, 12.\n')
    numbers = enter_numbers('Введите число')
    solution_task_3(numbers)


if __name__ == "__main__":
    menu.start_menu()


def enter_numbers(text, output_type=True):
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


def solution_task_1(value):
    """
    Функция решения первой задачи
    :param value: integer
    :return:
    """

    money_list, counters = list(randint(0, 1) for i in range(value)), [0, 0]
    print(f'{value} -> {" ".join(str(i) for i in money_list)}')
    for i in money_list:
        if i == 0:
            counters[0] += 1
        else:
            counters[1] += 1
    if counters[0] > counters[1]:
        print(f'{counters[1]}\n')
    elif counters[0] == counters[1]:
        print(f'{counters[1]}\n')
    else:
        print(f'{counters[0]}\n')


def solution_task_2(summa, product):
    """
    Функция решения второй задачи
    :param summa: int
    :param product: int
    :return:
    """
    # Первое решение
    # counting = ((summa / 2) ** 2 - product) ** 0.5
    # x, y = int(summa / 2 - counting), int(summa / 2 + counting)
    # print(f'{summa} {product} -> {x} {y}\n')

    # Второе решение с использованием math
    # counting = sqrt(((summa / 2) ** 2 - product))
    # x, y = int(summa / 2 - counting), int(summa / 2 + counting)
    # print(f'{summa} {product} -> {x} {y}\n')

    # Третье решение
    counting = []
    for i in range(summa + product):
        if i == (summa * i - product) ** 0.5:
            counting.append(i)
    print(summa, product, '->', *counting if len(counting) == 2 else counting + counting, '\n')


def solution_task_3(val):
    """
    Функция решения третьей задачи
    :param val: integer
    :return:
    """
    i = 1
    numbers_list = []
    while i <= val:
        numbers_list.append(i)
        i = i * 2
    print(f'{val} -> {" ".join(str(i) for i in numbers_list)}\n')
