# variant.py
# Индивидуальный вариант 5: Элементы, кратные 3

def selected_sum(matrix):
    """
    Возвращает сумму элементов матрицы, которые кратны 3.
    """
    total = 0
    for row in matrix:
        for val in row:
            if val % 3 == 0:
                total += val
    return total