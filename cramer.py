# Импорт модуля для работы с регулярными выражениями
import re

print('''
Это программа для решения системы линейных уравнений с тремя переменными.

Инструкция по использованию:
- Принимаются только целочисленные коэффициенты.
  Например: 2x
  Но не: 2.3x
- Вводите уравнение в порядке переменных. Переменная x должна быть первой, переменная y -- второй, переменная z -- третьей.
  Например: 3x + 2y - 7z = 15
  Но не: -7z + 3x + 2y = 15
- Добавляйте единицу в качестве коэффициента, если она подразумевается.
  Например: 1x + 2y + 1z = 1
  Но не: x + 2y + z = 1
''')

# Запрос на ввод уравнений
first_line = input('Введите первое уравнение: ')
second_line = input('Введите второе уравнение: ')
third_line = input('Введите третье уравнение: ')

# Все уравнения в одном списке
lines = [first_line, second_line, third_line]
# Все коэффициенты к каждому равнению в одну строку
line_coeffs = []
# Все коэффициенты по отдельности
coeffs = []


def det(matrix):
    ''' Функция для определения дискриминанта матрицы

    Принимает матрицу в виде списка со списками (строками матрицы).
    Вычисляет дискриминант по методу Крамера.
    '''
    return (int(matrix[0][0]) * int(matrix[1][1]) * int(matrix[2][2])) + (int(matrix[1][0]) * int(matrix[2][1]) * int(matrix[0][2])) + (int(matrix[0][1]) * int(matrix[1][2]) * int(matrix[2][0])) - (int(matrix[0][2]) * int(matrix[1][1]) * int(matrix[2][0])) - (int(matrix[0][1]) * int(matrix[1][0]) * int(matrix[2][2])) - (int(matrix[0][0]) * int(matrix[1][2]) * int(matrix[2][1]))


'''
Очичщаем уравнения от мусора:
- букв переменных и знаков равно
- пробелов после операторов
- двойных пробелов (образуются после удаления знака равенства)
'''
for line in lines:
    x = re.sub("[xyz=]", "", line)
    x = re.sub("[+][\s]", "+b", x)
    x = re.sub("[-][\s]", "-", x)
    x = re.sub("[\s][\s]", " ", x)
    line_coeffs.append(x)

# Разделяем коэффициенты в строке на четыре строки
for line_coeff in line_coeffs:
    coeffs.append(line_coeff.split(' ', 4))

# Дельта-переменные: общая, для x, для y и для z
delta = det([coeffs[0][:3], coeffs[1][:3], coeffs[2][:3]])
delta_x = det([[coeffs[0][3], coeffs[0][1], coeffs[0][2]], [coeffs[1][3],
                                                            coeffs[1][1], coeffs[1][2]], [coeffs[2][3], coeffs[2][1], coeffs[2][2]]])
delta_y = det([[coeffs[0][0], coeffs[0][3], coeffs[0][2]], [coeffs[1][0],
                                                            coeffs[1][3], coeffs[1][2]], [coeffs[2][0], coeffs[2][3], coeffs[2][2]]])
delta_z = det([[coeffs[0][0], coeffs[0][1], coeffs[0][3]], [coeffs[1][0],
                                                            coeffs[1][1], coeffs[1][3]], [coeffs[2][0], coeffs[2][1], coeffs[2][3]]])

# Вычисляем значения переменных
x = delta_x//delta
y = delta_y//delta
z = delta_z//delta

# Выводим значения переменных
print('x =', x)
print('y =', y)
print('z =', z)
