from Views.GetMenu import print_menu
from Controllers.NoteController import NoteController
from Models.NoteJson import ModelJSON
from Views.GetNote import View
from Models.Note import Note

import datetime


def start_menu():
    """
    Основная функция запуска программы.
    :return:
    """
    c = NoteController(ModelJSON("notes.json"), View())
    while (True):
        print('Программа заметки:')
        print_menu()
        task = ''
        try:
            task = int(input('Введите от 1 до 7: '))
        except:
            print('Косячник вводи цифру.')
        # Проверка введённого числа и запуск функции в основном фаиле
        if task == 1:
            print('\nСоздание заметки.')
            c.create_note(get_note_data())
        elif task == 2:
            print('\nПоказать заметку.')
            if c.notes_exist():
                c.show_note(int(get_number()))
        elif task == 3:
            if c.notes_exist():
                print('\nПоказать все заметки.')
                c.show_notes()
        elif task == 4:
            if c.notes_exist():
                print('\nРедактировать заметку.')
                updated_id = int(get_number())
                if c.note_id_exist(updated_id):
                    c.update_note(updated_id, get_note_data())
        elif task == 5:
            if c.notes_exist():
                print('\nВы удаляете заметку!')
                delete_id = int(get_number())
                if c.note_id_exist(delete_id):
                    c.delete_note(delete_id)
        elif task == 6:
            if c.notes_exist():
                print('Удалить все заметки!')
                if input('Уверены!!! (Y/N): ').capitalize() == 'Y':
                    if c.notes_exist():
                        c.delete_all_notes()
        elif task == 7:
            print('Выходим из программы')
            exit()
        else:
            print('Ошибка. Введите от 1 до 7.')


def get_note_data():
    note_id = 0
    date = datetime.datetime.now()
    title = input('\t\tДайте имя заметке: ')
    text = input('\t\tЗаполните заметку: ')
    return Note(note_id, date, title, text)


def get_number():
    while True:
        get_choice = input('\t\tВведите id заметки: ')
        if get_choice.isdigit() and int(get_choice) > 0:
            return get_choice
        else:
            print('\t\t\tВведено неверное id заметки!')
