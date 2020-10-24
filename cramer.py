import re
import copy

# Массив для коэффициентов при переменных
coeffs = []
# Массив для свободных коэффициентов
free_coeffs = []

def determinant(matrix, n):
    # Определитель единичной матрицы —
    # её единственный элемент
    if n == 1:
        return(matrix[0][0])
    # Если размерность матрицы равна двум,
    # то считаем определитель по специальной формуле
    elif n == 2:
        return(matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1])
    # Если размерность матрицы больше двух,
    # то рекурсивно считаем определитель
    # более маленьких матриц, размерность
    # которых постепенно доводим до двух
    else:
        c = 0
        for i in range(n):
            new_matrix = copy.deepcopy(matrix)
            new_matrix.pop(0)
            for j in range(n-1):
                new_matrix[j].pop(i)
            c += (-1)**i * matrix[0][i] * determinant(new_matrix, n - 1)
        return(c)

number = int(input('Сколько уравнений? '))

for i in range(number):
    # Пустой массив, где будут коэффициенты
    coeffs.append([])
    for j in range(number):
        # Собираем коэффициенты
        coeffs[i].append(int(input(f'Введите {j+1}-й коэффициент {i+1}-го уравнения: ')))
    # Собираем свободные коэффициенты
    free_coeffs.append(int(input(f'Введите свободный коэффициент {i+1}-го уравнения: ')))

# Определитель матрицы
det = determinant(coeffs, number)

if det == 0:
    print("Определитель равен нулю")
else:
    # Для матрицы с ненулевым определителем
    for i in range(number):
        # Для каждой переменной
        line = copy.deepcopy(coeffs)
        for j in range(number):
            # Заменяем столбец с коэффициентами
            # при переменной на свободные
            line[j][i] = free_coeffs[j]
        # Находим определитель матрицы с заменёнными
        # коэффициентами
        line_det = determinant(line, number)
        # Выводим результаты переменных
        print(f'Переменная {i+1}: {line_det/det}')
        
