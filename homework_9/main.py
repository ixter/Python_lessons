import menu  # менюшка
import sys
import pygame
import telebot
from telebot import types
import csv
import math


def task_1():
    print(
        'Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP\n'
    )
    pygame.init()  # инициализируем библиотеку
    size_block = (100)  # размер блока
    margin = 5  # отступы
    width = height = size_block * 3 + margin * 4  # высота и ширина блока и оступов
    size_window = (width, height)  # размер окна
    screen = pygame.display.set_mode(size_window)  # задаём окну размер
    pygame.display.set_caption("Крестики-нолики")  # задаём окну заглавие

    black = (0, 0, 0)  # чёрный
    red = (255, 0, 0)  # красный
    green = (0, 255, 0)  # зёлёный
    white = (255, 255, 255)  # белый
    gray = (211, 211, 211)  # серый
    field_game = [[0] * 3 for i in range(3)]  # массив поля 3*3 заполненный 0
    query = 0  # 1 2 3 4 5 6 7  чередование ходов
    game_over = False  # флаг окончания игры
    screen.fill(gray)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # ловим ивент на закрытие окна и убиваем приложение
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:  # клик мышки и не геймовер
                x_mouse, y_mouse = pygame.mouse.get_pos()  # получение позиции по х,у мышки
                col = x_mouse // (size_block + margin)  # номер колонки по которой кликнули
                row = y_mouse // (size_block + margin)  # номер строки по которой кликнули
                if field_game[row][col] == 0:  # если строка и колонка пустые
                    if query % 2 == 0:  # проверяем на чётность
                        field_game[row][col] = 'x'  # и рисуем крестик
                    else:  # иначе
                        field_game[row][col] = 'o'  # рисуем нолик
                    query += 1  # чередуем ход
            # иначе если нажали клавишу и нажали пробел 
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_over = False  # заканчиваем игру
                field_game = [[0] * 3 for i in range(3)]  # обнуляем массив
                query = 0  # сбрасываем чередование
                screen.fill(black)  # заполняем чёрным цветом окно
        if not game_over:  # если не геймовер
            for row in range(3):  # обход строк
                for col in range(3):  # обход колонок
                    if field_game[row][col] == 'x':  # если колонка и строка х
                        color = red  # красим в красный
                    elif field_game[row][col] == 'o':  # если колонка и строка х
                        color = green  # красим в зелёный
                    else:
                        color = black  # красим в белый
                    x = col * size_block + (col + 1) * margin  # колонка + размер блока +(номер колонки+1)* кол отступов
                    y = row * size_block + (row + 1) * margin  # строка + размер блока +(номер строки+1)* кол отступов
                    pygame.draw.rect(screen, color,
                                     (x, y, size_block, size_block))  # экран, цвет,(координаты верх левый, низ правый)
                    if color == red:  # если цвет красный
                        # рисуем крестик по координатам
                        pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 5)
                        pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 5)
                    elif color == green:  # если цвет зелёный
                        # рисуем кружок по координатам
                        pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2),
                                           size_block // 2 - 3,
                                           5)
        if (query - 1) % 2 == 0:  # x
            game_over = check_win(field_game, 'x')  # проверяем на победу х
        else:
            game_over = check_win(field_game, 'o')  # проверяем на победу у
        if game_over:  # если геймовер
            screen.fill(black)  # заполняем чёрным цветом экран
            font = pygame.font.SysFont('stxingkai', 80)  # указываем шрифт и размер
            text1 = font.render(game_over, True, white)  # рендерим шрифт
            text_rect = text1.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text1, [text_x, text_y])
        pygame.display.update()  # обновляем экран


def check_win(field_game, sign):
    """
    Функция проверки на победу
    :param field_game: 
    :param sign: 
    :return: 
    """
    nulls = 0
    for row in field_game:
        nulls += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if field_game[0][col] == sign and field_game[1][col] == sign and field_game[2][col] == sign:
            return sign
    if field_game[0][0] == sign and field_game[1][1] == sign and field_game[2][2] == sign:
        return sign
    if field_game[0][2] == sign and field_game[1][1] == sign and field_game[2][0] == sign:
        return sign
    if nulls == 0:
        return 'Ничья'
    return False


def task_2():
    print("""Прикрутить бота к задачам с предыдущего семинара:
Создать калькулятор для работы с рациональными и комплексными числами, 
организовать меню, добавив в неё систему логирования"""
          )
    bot.polling()


if __name__ == "__main__":
    menu.start_menu()


def get_token():
    with open('token.txt', 'r') as file:
        return file.read()


bot = telebot.TeleBot(get_token())

value = ''
old_value = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
             telebot.types.InlineKeyboardButton('C', callback_data='C'),
             telebot.types.InlineKeyboardButton('<=', callback_data='<='),
             telebot.types.InlineKeyboardButton('/', callback_data='/'))
keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
             telebot.types.InlineKeyboardButton('8', callback_data='8'),
             telebot.types.InlineKeyboardButton('9', callback_data='9'),
             telebot.types.InlineKeyboardButton('*', callback_data='*'))
keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
             telebot.types.InlineKeyboardButton('5', callback_data='5'),
             telebot.types.InlineKeyboardButton('6', callback_data='6'),
             telebot.types.InlineKeyboardButton('-', callback_data='-'))
keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
             telebot.types.InlineKeyboardButton('2', callback_data='2'),
             telebot.types.InlineKeyboardButton('3', callback_data='3'),
             telebot.types.InlineKeyboardButton('+', callback_data='+'))
keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
             telebot.types.InlineKeyboardButton('0', callback_data='0'),
             telebot.types.InlineKeyboardButton(',', callback_data='.'),
             telebot.types.InlineKeyboardButton('=', callback_data='='))


@bot.message_handler(commands=['start', 'go'])
def getMessage(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id,
                         '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id,
                         value, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data
    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value) - 1]
    elif data == '=':
        value = str(eval(value))
    else:
        value += data
    if value != old_value:
        if value == '':
            bot.edit_message_text(
                chat_id=query.message.chat.id, message_id=query.message.id, text='0', reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.id, text=value, reply_markup=keyboard)
        old_value = value


def task_3():
    print("""Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)""")
    with open("simple_data/california_housing_train.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            if int(float(row['population'])) <= 500:
                print(int(float(row['population'])), '<--популяция | средняя стоимость дома -->',
                      int(float(row['median_house_value'])))


def task_4():
    print("""Задача 42: Узнать какая максимальная households в зоне минимального значения population""")
    with open("simple_data/california_housing_train.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        array_pop = {}
        counter = 0
        for row in reader:
            if int(float(row['population'])) <= 500:
                array_pop[counter] = (int(float(row['population'])))
                counter += 1
        print(max(array_pop), "<-- максимальная households в зоне минимального значения population")
