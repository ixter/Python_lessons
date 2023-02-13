import menu  # менюшка


def task_1():
    print(
        'Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.\n'
        'A = 3; B = 5 -> 243 (3⁵)\n'
        'A = 2; B = 3 -> 8\n'
    )
    number_one = enter_numbers('Введите A')
    number_two = enter_numbers('Введите B')
    indexes = {
        "0": "\u2070", "1": "\u00B9", "2": "\u00B2", "3": "\u00B3", "4": "\u2074", "5": "\u2075", "6": "\u2076",
        "7": "\u2077", "8": "\u2078", "9": "\u2079"
    }
    print(
        f'A = {number_one}; B = {number_two} -> '
        f'{solution_task_1(number_one, number_two)} ({number_one}{indexes[str(number_two)] or ""})\n')


def task_2():
    print('Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.\n'
          'Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.\n'
          '2 2\n'
          '4\n'
          )
    number_one = enter_numbers('Введите A')
    number_two = enter_numbers('Введите B')
    print(f'{number_one} {number_two}\n{solution_task_2(number_one, number_two)}\n')


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


def solution_task_1(val_one: int, val_two: int) -> int:
    """
    Функция решения первой задачи
    :param val_one: int
    :param val_two: int
    :return: int
    """
    if val_two == 1:
        return val_one
    else:
        return val_one * solution_task_1(val_one, val_two - 1)


def solution_task_2(val_one: int, val_two: int) -> int:
    """
    Функция решения второй задачи
    :param val_one: int
    :param val_two: int
    :return: int
    """
    if val_two == 0:
        return val_one
    else:
        return solution_task_2(val_one + 1, val_two - 1)
