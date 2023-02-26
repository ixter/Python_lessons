import menu  # менюшка


def task_1():
    print(
        'Задача 1. Напишите функцию read_last(lines, file),\n'
        'которая будет открывать определенный файл file и выводить на печать\n'
        'построчно последние строки в количестве lines (на всякий случай проверим,\n'
        'что задано положительное целое число).\n'
        'Протестируем функцию на файле «article.txt» со следующим содержимым:\n'
        'Вечерело\n'
        'Жужжали мухи\n'
        'Светил фонарик\n'
        'Кипела вода в чайнике\n'
        'Венера зажглась на небе\n'
        'Деревья шумели\n'
        'Тучи разошлись\n'
        'Листва зеленела\n'
    )
    file = enter_numbers('Введите имя файла(article.txt)', False)
    lines = enter_numbers('Сколько последних строк вывести')
    if lines > 0 and file == 'article.txt':
        solution_task_1(lines, file)
    else:
        print('Неверно указаны последние строки')


def task_2():
    print('Задача 2.\n'
          'Документ «article.txt» содержит следующий текст:\n'
          'Вечерело\n'
          'Жужжали мухи\n'
          'Светил фонарик\n'
          'Кипела вода в чайнике\n'
          'Венера зажглась на небе\n'
          'Деревья шумели\n'
          'Тучи разошлись\n'
          'Листва зеленела\n'
          'Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину\n'
          '(или список слов, если таковых несколько).\n'
          )
    file = enter_numbers('Введите имя файла(article.txt)', False)
    if file and file == 'article.txt':
        solution_task_2(file)
    else:
        print('Неверно указано название фаила')


def task_3():
    print('ДОП ЗАДАЧА.\n'
          'Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста. У нас труб будет больше.\n'
          'Бассейн можно заполнить из N труб.\n'
          'В файле pipes.txt записаны времена заполнения всего бассейна только одной данной работающей трубой (в часах).\n'
          'Затем после пустой строки перечислены трубы, которые будут заполнять бассейн.\n'
          'Сколько минут на это потребуется?\n'
          'Номер трубы соответствует номеру строки, в которой записана ее производительность.\n'
          'Результат запишите в файл time.txt\n'
          'Пример\n'
          'Ввод\n'
          '1\n'
          '2\n'
          '3\n'
          '(пустая строка)\n'
          '1 2 3\n'
          'Вывод\n'
          '32.72727272727273\n'
          )
    solution_task_3()


def task_4():
    print("""Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной"""
          )
    solution_task_4()


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


def solution_task_1(val_one: int, val_two: str):
    """
    Функция решения первой задачи
    :param val_one: int
    :param val_two: str
    """
    with open(val_two, 'r', encoding='utf-8') as file:
        text = file.read().splitlines()
        max = len(text)
        if val_one > max:
            min = 0
            print('Не верно указано количество последних строк\n'
                  f'Будет выведен максимум в {max} строк\n'
                  )
        else:
            min = len(text) - val_one
        for e in range(min, max):
            print(text[e])
        print('\n')


def solution_task_2(val_one: str):
    """
    Функция решения второй задачи
    :param val_one: str
    """
    with open(val_one, 'r', encoding='utf-8') as file:
        text = set(file.read().split())
        text = list(sorted(text, key=len, reverse=True))
        print(text[0])
        for i in range(1, len(text)):
            if len(text[0]) == len(text[i]):
                print(text[i])
            else:
                break


def solution_task_3():
    """
    Функция решения третьей задачи
    """
    # with open('pipes.txt', encoding='utf-8') as file:
    #     time = file.read().split('\n')
    # while all(time) is False:
    #     time.remove('')
    # pipes = list(map(int, time[-1].split()))
    # time.remove(time[-1])
    # pipes = list(map(lambda x: x - 1, pipes))
    # time = [time[pipe] for pipe in pipes]
    # with open('time.txt', 'w', encoding='utf-8') as answer:
    #     answer.write(str(60 / sum(map(lambda x: 1 / float(x), time))))

    f = open('pipes.txt', 'r')
    f2 = open("time.txt", "w")
    s = [line.rstrip() for line in f]
    d = []
    d1 = []
    flag = 0
    for i in s:
        if flag == 0:
            if i != '':
                d.append(eval(i))
            else:
                flag += 1
        else:
            s1 = i.split()
            for j in s1:
                d1.append(d[int(j) - 1])
    f2.write(str(60 / sum([1 / i for i in d1])))
    f2.close()
    f.close()


def solution_task_4():
    """
    Функция решения четвёртой задачи
    """
    file = 'phonebook.txt'
    choose_action(file)


def choose_action(phonebook):
    while True:
        print('Что вы хотите сделать?')
        user_choice = input('1 - Импортировать данные\n2 - Найти контакт\n3 - Добавить контакт\n\
4 - Изменить контакт\n5 - Удалить контакт\n6 - Просмотреть все контакты\n0 - Выйти из приложения\n')
        print()
        if user_choice == '1':
            file_to_add = input('Введите название импортируемого файла: ')
            import_data(file_to_add, phonebook)
        elif user_choice == '2':
            contact_list = read_file_to_dict(phonebook)
            find_number(contact_list)
        elif user_choice == '3':
            add_phone_number(phonebook)
        elif user_choice == '4':
            change_phone_number(phonebook)
        elif user_choice == '5':
            delete_contact(phonebook)
        elif user_choice == '6':
            show_phonebook(phonebook)
        elif user_choice == '0':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue


def import_data(file_to_add, phonebook):
    try:
        with open(file_to_add, 'r', encoding='utf-8') as new_contacts, open(phonebook, 'a', encoding='utf-8') as file:
            contacts_to_add = new_contacts.readlines()
            file.writelines(contacts_to_add)
    except FileNotFoundError:
        print(f'{file_to_add} не найден')


def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list


def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list


def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите номер для поиска: ')
        print()
    return search_field, search_value


def find_number(contact_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()


def get_new_number():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, phone_number


def add_phone_number(file_name):
    info = ' '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')


def show_phonebook(file_name):
    list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts


def search_to_modify(contact_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()


def change_phone_number(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
    if field == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите имя: ')
    elif field == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    contact_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def delete_contact(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()
