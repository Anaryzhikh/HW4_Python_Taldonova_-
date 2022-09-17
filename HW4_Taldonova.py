# 1. ввести число и округлить его до 0,0001
# 2. алгоритмом. простые числа - числа, которые делятся только на 1 и на самого себя
# 3. через множества. функция set
# 4. найти в библиотеке

# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# Помогите разобраться, как к числу "a" добавлять нули в конце, если знаков после запятой в нем меньше, чем в "d"?

# import math
# a = float(input('Введите число: '))
# d = float(input('Введите точность округления: '))
# def get_precision(f):
#     str_f = str(f)
#     if '.' not in str_f:
#         return 0
#     return len(str_f[str_f.index('.') + 1:])
# print(round(a, int(get_precision(d))))

# 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

# number = int(input('введите число: '))
# divisor = 2
# list = []
# while divisor <= number:
#     if (number % divisor) == 0:
#         list.append(divisor)
#         number = number//divisor
#     else:
#         divisor += 1
# print(list)

# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

# numbers = []
# for i in input().split():
#     numbers.append(int(i))
# print(numbers)
# unique_numbers = list(set(numbers))
# print(unique_numbers)

# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Подскажите, как убрать запятые и квадратные скобки из результата?

# with open('poly_1.txt', 'w', encoding='utf-8') as file:
#     file.write('5*x^3 + 8*x^2')
#
# with open('poly_2.txt', 'w', encoding='utf-8') as file:
#     file.write('10*x^4 + 6*x^3')
#
# with open('poly_1.txt', 'r') as file:
#     poly_1 = file.readline()
#     list_of_poly_1 = poly_1.split()
#
# with open('poly_2.txt', 'r') as file:
#     poly_2 = file.readline()
#     list_of_poly_2 = poly_2.split()
#
# print(f'{list_of_poly_1} + {list_of_poly_2}')
# sum_poly = list_of_poly_1 + list_of_poly_2
#
# with open('sum_poly.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{list_of_poly_1} + {list_of_poly_2}')