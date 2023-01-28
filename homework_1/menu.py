import main

menu_options = {
    1: 'Задача 2',
    2: 'Задача 4',
    3: 'Задача 6',
    4: 'Задача 8',
    5: 'Exit',
}


def print_menu():
    """
    Функция отрисовки меню в консоль
    :return:
    """
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

def start_menu():
    """
    Основная функция запуска программы.
    :return:
    """
    while (True):
        print_menu()
        task = ''
        try:
            task = int(input('Введите от 1 до 5: '))
        except:
            print('Косячник вводи цифру.')
        # Проверка введённого числа и запуск функции в основном фаиле
        if task == 1:
            main.task_1()
        elif task == 2:
            main.task_2()
        elif task == 3:
            main.task_3()
        elif task == 4:
            main.task_4()
        elif task == 5:
            print('Выходим из программы')
            exit()
        else:
            print('Ошибка. Введите от 1 до 5.')
