# # 1. Сумма трех
# # Посчитайте сумму трех введенных целых чисел
# def sum_three_char():
#     a = int(input('a = '))
#     b = int(input('b = '))
#     c = int(input('c = '))
#     print(f'Сумма {a + b + c}')
#
#
# # 2. Площадь
# # Пользователь вводит стороны прямоугольника, выведите его площадь
# def square_rectangle():
#     a = int(input('a = '))
#     b = int(input('b = '))
#     print(f'Площадь прямоугольника {a * b}')
#
#
# # 3. Периметр
# # Пользователь вводит стороны прямоугольника, выведите его периметр
# # P = 2 × (a + b)
# def rectangle_perimeter():
#     a = int(input('a = '))
#     b = int(input('b = '))
#     print(f'Периметр прямоугольника {2 * (a + b)}')
#
#
# if __name__ == '__main__':
#     job = int(input('Выберите задачу: 1,2,3: '))
#     if job == 1:
#         sum_three_char()
#     if job == 2:
#         square_rectangle()
#     if job == 3:
#         rectangle_perimeter()


# a = int(input())
# if 1000 <= a <= 9999 or -9999 <= a <= -1000:
#     print('YES')
# else:
#     print("No")


# 1. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
#
# **Input:**
# n = 700
# m = 750
# **Output:**
# 2

# n = 700
# m = 750
# print((m+n-1)//n)

# 3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
#
# **Input:**
# 20  10*2
# 21  10*2 +1
# 22
# **Output:**
# 32
# x = 20
# y = 21
# z = 22
#
# if x // 2 != 0:
#     x += 1
# if y // 2 != 0:
#     y += 1
# if z // 2 != 0:
#     z += 1
# print(x // 2 + y // 2 + z // 2)
# с урока
# print(x // 2 + x % 2 + y // 2 + y % 2 + z // 2 + z % 2)

# 7. Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем,
# год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# **Input:**
# 2016
# **Output:**
# YES
# a = 2016
#
# if a % 4 == 0 and a % 100 != 0 and a % 400 == 0:
#     print('YES')
