import menu  # менюшка
from random import randint
from math import sqrt


def task_1():
    print('Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].\n'
          'Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.\n'
          ' В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X\n'
          'пример\n'
          '5\n'
          '12345\n'
          '3\n'
          '-> 1\n'
          )
    number = enter_numbers('Введите число N')
    solution_task_1(number)


def task_2():
    print('Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.\n'
          'Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.\n'
          'В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X\n'
          'пример\n'
          '5\n'
          '1 2 3 4 5\n'
          '6\n'
          '-> 5\n'
          )
    number = enter_numbers('Введите число N')
    solution_task_2(number)


def task_3():
    print(
        'Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.\n'
        'В случае с английским алфавитом очки распределяются так:\n'
        'A, E, I, O, U, L, N, S, T, R – 1 очко;\n'
        'D, G – 2 очка;\n'
        'B, C, M, P – 3 очка;\n'
        'F, H, V, W, Y – 4 очка;\n'
        'K – 5 очков;\n'
        'J, X – 8 очков;\n'
        'Q, Z – 10 очков.\n'
        'А русские буквы оцениваются так:\n'
        'А, В, Е, И, Н, О, Р, С, Т – 1 очко;\n'
        'Д, К, Л, М, П, У – 2 очка;\n'
        'Б, Г, Ё, Ь, Я – 3 очка;\n'
        'Й, Ы – 4 очка;\n'
        'Ж, З, Х, Ц, Ч – 5 очков;\n'
        'Ш, Э, Ю – 8 очков;\n'
        'Ф, Щ, Ъ – 10 очков.\n'
        'Напишите программу, которая вычисляет стоимость введенного пользователем слова.\n'
        'Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.\n'
        '\n'
        'пример\n'
        '\n'
        'Ввод:\n'
        'ноутбук\n'
        'Вывод:\n'
        '12\n')
    word = enter_numbers('Введите слово', False)
    solution_task_3(word)


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
    n_list, counter = [], 0
    print(value)
    for i in range(1, (value + 1)):
        n_list.append(i)
    print(*n_list)
    find = enter_numbers(f'Введите число от 1 до {value}')
    if value >= find >= 1:
        print(f'-> {n_list.count(find)}\n')
    else:
        print('Не верно указано число\n')


def solution_task_2(value):
    """
    Функция решения второй задачи
    :param value: int
    :return:
    """
    n_list, counter = [], 0
    print(value)
    for i in range(1, (value + 1)):
        n_list.append(i)
    print(*n_list)
    find = enter_numbers('Введите X')
    print(f'-> {nearest_value(n_list, find)}\n')


def nearest_value(values: list, one: int) -> int:
    return min(values, key=lambda n: (abs(one - n), n))


# https://habr.com/ru/company/piter/blog/674234/  лямбда функция

def solution_task_3(val):
    """
    Функция решения третьей задачи
    :param val: string
    :return:
    """
    count = 0
    alphabet = {
        1: 'А, В, Е, И, Н, О, Р, С, Т, A, E, I, O, U, L, N, S, T, R',
        2: 'Д, К, Л, М, П, У, D, G',
        3: 'Б, Г, Ё, Ь, Я, B, C, M, P',
        4: 'Й, Ы, F, H, V, W, Y',
        5: 'Ж, З, Х, Ц, Ч, K',
        8: 'Ш, Э, Ю, J, X',
        10: 'Ф, Щ, Ъ, Q, Z'
    }
    for i in val.upper():
        for j in alphabet.items():
            if i in j[1]:
                count += j[0]
    print(f'Стоимость слова: {val} = {count}')
