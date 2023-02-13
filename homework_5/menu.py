import main

menu_options = {
    1: 'Задача 26',
    2: 'Задача 28',
    3: 'Exit',
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
            task = int(input('Введите от 1 до 3: '))
        except:
            print('Косячник вводи цифру.')
        # Проверка введённого числа и запуск функции в основном фаиле
        if task == 1:
            main.task_1()
        elif task == 2:
            main.task_2()
        elif task == 3:
            print('Выходим из программы')
            exit()
        else:
            print('Ошибка. Введите от 1 до 3.')
