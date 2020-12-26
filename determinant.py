import copy

def main():
    matrix = []

    # Спрашиваем и выводим размер матрицы
    n = int(input('Введите размер матрицы: '))

    # Если введённое число больше нуля,
    # работаем с матрицей
    if n > 0:
        print('Размер введённой матрицы — ', n)

        # Заполняем матрицу
        for i in range(n):
            matrix.append([])
            for j in range(n):
                x = int(input(f'Введите {j+1}-й элементы {i+1}-й строки: '))
                matrix[i].append(x)

        # Выводим матрицу
        print('Введённая матрица: ')
        for i in range(n):
            string = ''
            for j in range(n):
                string += str(matrix[i][j]) + ' '
            print(string)
        
        # Выводим определитель матрицы
        print('Определитель матрицы:', determinant(matrix, n))
    # Если введённое число неположительно,
    # выводим сообщение об ошибке
    else:
        print('Ошибка ввода, размер матрицы должен быть положительным')

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

main()