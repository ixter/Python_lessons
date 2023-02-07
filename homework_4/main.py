import menu  # менюшка
from random import randint


def task_1():
    print('Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с\n'
          'повторениями). Выдать без повторений в порядке возрастания все те числа, которые\n'
          'встречаются в обоих наборах.\n'
          'Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во\n'
          'элементов второго множества. Затем пользователь вводит сами элементы множеств.\n'
          '11 6\n'
          '2 4 6 8 10 12 10 8 6 4 2\n'
          '3 6 9 12 15 18\n'
          '6 12\n'
          )
    number_one = enter_numbers('Введите из скольки элементов будет первый набор чисел n')
    number_two = enter_numbers('Введите из скольки элементов будет второй набор чисел m')
    solution_task_1(number_one, number_two)


def task_2():
    print('Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.\n'
          'Она растет на круглой грядке, причем кусты высажены только по окружности.\n'
          'Таким образом, у каждого куста есть ровно два соседних.\n'
          'Всего на грядке растет N кустов.\n'
          'Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них\n'
          'выросло различное число ягод – на i-ом кусте выросло ai ягод.\n'
          'В этом фермерском хозяйстве внедрена система автоматического сбора черники.\n'
          'Эта система состоит из управляющего модуля и нескольких собирающих модулей.\n'
          'Собирающий модуль за один заход, находясь непосредственно перед некоторым\n'
          'кустом, собирает ягоды с этого куста и с двух соседних с ним.\n'
          'Напишите программу для нахождения максимального числа ягод, которое может\n'
          'собрать за один заход собирающий модуль, находясь перед некоторым кустом\n'
          'заданной во входном файле грядки.\n'
          '4 -> 1 2 3 4\n'
          '9\n'
          )
    number = enter_numbers('Введите число N')
    solution_task_2(number)


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


def solution_task_1(val_one, val_two):
    """
    Функция решения первой задачи
    :param val_one:
    :param val_two:
    :return:
    """
    '11 6\n'
    '2 4 6 8 10 12 10 8 6 4 2\n'
    '3 6 9 12 15 18\n'
    '6 12\n'
    # Генерим множества
    n = set({randint(1, 30) for i in range(val_one)})
    m = set({randint(1, 30) for i in range(val_two)})
    # Выводим без скобок множества
    print(*n)
    print(*m)
    # Сортируем и сравниваем с распаковкой без скобок
    print(*sorted(n & m))


def solution_task_2(value):
    """
    Функция решения второй задачи
    :param value: int
    :return:
    """
    # berries = [randint(1, 6) for i in range(value)]
    berries = [1, 2, 3, 4]
    print(value, ' -> ', *berries)
    value = len(berries)
    berries = berries + berries[:2]
    max_berries = 0
    for i in range(value):
        max_berries = max(max_berries, berries[i] + berries[i + 1] + berries[i + 2])
    print(f'{max_berries}\n')
