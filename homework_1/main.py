import menu  # менюшка


def task_1():
    print('Задача 2: Найдите сумму цифр трехзначного числа.\n'
          '123 -> 6 (1 + 2 + 3)\n'
          '100 -> 1 (1 + 0 + 0)\n')
    numbers = enter_numbers('Введите трехзначное число')
    solution_task_1(numbers)


def task_2():
    print('Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. \n'
          'Сколько журавликов сделал каждый ребенок, если известно,\n'
          'что Петя и Сережа сделали одинаковое количество журавликов,\n'
          'а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?\n'
          '6 -> 1  4  1\n'
          '24 -> 4  16  4\n'
          '60 -> 10  40  10\n')
    numbers = enter_numbers('Введите количество сделанных журавликов')
    solution_task_2(numbers)


def task_3():
    print('Задача 6: Вы пользуетесь общественным транспортом? Вероятно, \n'
          'вы расплачивались за проезд и получали билет с номером.\n'
          'Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.\n'
          'Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.\n'
          'Вам требуется написать программу, которая проверяет счастливость билета.\n'
          '385916 -> yes\n'
          '123456 -> no\n')
    numbers = enter_numbers('Введите номер билета')
    solution_task_3(numbers)


def task_4():
    print('Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,\n'
          ' если разрешается сделать один разлом по прямой между дольками \n'
          '(то есть разломить шоколадку на два прямоугольника).\n'
          '3 2 4 -> yes\n'
          '3 2 1 -> no\n')
    list_numbers = enter_numbers('Введите размер шоколадки через пробел или запятую n m и k долек\n'
                                 'для примера 3 2 4 и ввод', False)
    list_numbers = list_numbers.replace(' ', ',').split(',', 3)
    solution_task_4(list_numbers)


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
    if 100 <= value <= 999:
        d1 = value % 10
        d2 = value % 100 // 10
        d3 = value // 100
        summary = d1 + d2 + d3
        print(f'{value} -> {summary} ({d3} + {d2} + {d1})\n')
    else:
        print('Не корректно введено число, необходимое число должно быть в пределах от 100 до 999\n')


def solution_task_2(val):
    """
    Функция решения второй задачи
    :param val: integer
    :return:
    """
    if val % 3 == 0:
        t = val // 6
        o = (t + t) * 2
        total = t + o + t
        f_word = f'{val} -> {t}  {o}  {t}'
        if total == val:
            print(f'{f_word}\n')
        else:
            print(f'{f_word}, а {val - total} потерялись\n')
    else:
        print(f'Введено не корректное число\n')


def solution_task_3(val):
    """
    Функция решения третьей задачи
    :param val: integer
    :return:
    """
    if 100000 <= val <= 999999:
        first_three_digits = 0
        second_three_digits = 0
        ticket = val
        for i in range(6):
            if i < 3:
                first_three_digits += val % 10
            else:
                second_three_digits += val % 10
            val = int(val / 10)
        if first_three_digits == second_three_digits:
            print(f'{ticket} -> Счастливый\n')
        else:
            print(f'{ticket} -> Не счастливый\n')
    else:
        print(f'Введено не корректное число\n')


def solution_task_4(val):
    """
    Функция решения четвёртой задачи
    :param val: Список
    :return:
    """
    val = check_data(val)
    if val is not None:
        try:
            x = int(val[0])
            y = int(val[1])
            z = int(val[2])
            if z < x * y and ((z % x == 0) or (z % y == 0)):
                print(f'{x} {y} {z} -> Да')
            else:
                print(f'{x} {y} {z} -> Нет')
        except:
            print(f'Введены не корректные значения\n')


def check_data(text):
    """
    Функция проверки корректности введённых данных
    Например введено чило слитно 324
    Или введено меньше символов
    Корректные значения для ввода:
     324
     3 2 4
     3,2,4
     3, 2, 4
    :param text: Список
    :return: Список из 3 значений ['3', '2', '4']
    """
    val = None
    if len(text) == 1 and len(list(text[0])) == 3:
        val = list(text[0])
    elif len(text) == 3:
        val = text
    else:
        print(f'Не корректно введены вводные параметры\n')
    return val
