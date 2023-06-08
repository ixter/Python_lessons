import json
import os.path
from Models.Note import Note
from Views.GetNote import View

class ModelJSON(object):

    def __init__(self, filename):
        self.filename = filename
        self.notes = list()

    def create_note(self, note):
        """
        Создание заметки
        :param note: object Заметка
        :return: запись в фаил
        """
        self.notes = self.read_notes()
        max_id = 0
        for item in self.notes:
            if item.note_id > max_id:
                max_id = item.note_id
        note_id = max_id + 1
        note.note_id = note_id

        self.notes.append(note)
        self.write_json(self.notes)

    def read_note(self, search_id):
        """
        Чтение заметки по айди
        :param search_id: int
        :return: object заметка
        """
        self.notes = self.read_notes()
        for note in self.notes:
            if note.note_id == search_id:
                return note
        else:
            View.display_note_id_not_exist(search_id)

    def read_notes(self):
        """
        чтение json фаила заметок
        :return:
        """
        return self.read_json()

    def update_note(self, search_id, note):
        """
        Обновление заметки по id
        :param search_id: int id заметки
        :param note: object сама заметка
        :return: сохранение в фаил
        """
        self.notes = self.read_notes()
        for item in self.notes:
            if item.note_id == search_id:
                item.date = note.date
                item.title = note.title
                item.text = note.text

        self.write_json(self.notes)

    def delete_note(self, search_id):
        """
        Удаление заметки по id
        :param search_id: int id
        :return: запись в фаил
        """
        self.notes = self.read_notes()

        for index, note in enumerate(self.notes):
            if note.note_id == search_id:
                del self.notes[index]

        self.write_json(self.notes)

    def delete_all_notes(self):
        """
        Удаление всех заметок
        :return: Запись в фаил
        """
        self.notes = self.read_notes()
        self.notes.clear()
        self.write_json(self.notes)

    def write_json(self, notes):
        """
        Запись в фаил заметок
        :param notes: object заметки
        :return: Запись в фаил
        """
        json_strings_list = list()
        for note in notes:
            json_strings_list.append({'id': note.note_id, 'date': note.date, 'title': note.title, 'text': note.text})

        notes_json = json.dumps(json_strings_list, indent=4, ensure_ascii=False, sort_keys=False, default=str)

        with open(os.path.dirname(__file__) + '/../Files/' + self.filename, "w", encoding='utf-8') as my_file:
            my_file.write(notes_json)

    def read_json(self):
        """
        Чтение из фаила
        :return: object
        """
        notes_list = list()
        try:
            with open(os.path.dirname(__file__) + '/../Files/' + self.filename, "r", encoding='utf-8') as my_file:
                notes_json = my_file.read()
            data = json.loads(notes_json)
            data.sort(key=lambda x: x['date'])
            for item in data:
                notes_list.append(Note(item['id'], item['date'], item['title'], item['text']))

            return notes_list
        except ValueError:
            return self.notes
