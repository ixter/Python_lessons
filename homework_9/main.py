import menu  # менюшка


def task_1():
    print(
        'Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.\n'
        'Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,\n'
        'Вам стоит написать программу.\n'
        'Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)\n'
        'в каждой фразе стихотворения одинаковое.\n'
        'Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.\n'
        'Фразы отделяются друг от друга пробелами.\n'
        'Стихотворение  Винни-Пух вбивает в программу с клавиатуры.\n'
        'В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,\n'
        'если с ритмом все не в порядке\n'
        'Ввод:\n'
        'пара-ра-рам рам-пам-папам па-ра-па-да\n'
        'Вывод:\n'
        'Парам пам-пам\n'
    )
    number_one = enter_numbers('Введите стих', False)
    solution_task_1(number_one)


def task_2():
    print('Задача 36:   Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),\n'
          'которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.\n'
          'Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.\n'
          'Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).\n'
          'Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,\n'
          'как, например, у операции умножения.\n'
          'Ввод:\n'
          'print_operation_table(lambda x, y: x * y)\n'
          'Вывод:\n'
          '1 2 3 4 5 6\n'
          '2 4 6 8 10 12\n'
          '3 6 9 12 15 18\n'
          '4 8 12 16 20 24\n'
          '5 10 15 20 25 30\n'
          '6 12 18 24 30 36\n'
          )
    solution_task_2(lambda x, y: x * y)


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


def solution_task_1(val_one: str):
    """
    Функция решения первой задачи
    :param val_one: str
    """
    verse = val_one.split(' ')
    print(*verse)
    vowels = ('а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы')
    fin = []
    for el in verse:
        count = 0
        for letter in el:
            if letter in vowels:
                count += 1
        fin.append(count)
    if len(set(fin)) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')


def solution_task_2(values, val_one: int = 6, val_two: int = 6):
    """
    Функция решения второй задачи
    :param values:
    :param val_one: int
    :param val_two: int
    """
    for i in range(1, val_one + 1):
        for j in range(1, val_two + 1):
            print(values(i, j), end=' ')
        print()
