from Models.Menu import menu_options


def print_menu():
    """
    Функция отрисовки меню в консоль
    :return:
    """
    for key in menu_options.keys():
        print(key, '--', menu_options[key])
