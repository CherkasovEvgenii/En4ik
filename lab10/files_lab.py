# files_lab.py

def read_matrix(path):
    """
    Читает матрицу из файла. 
    Выбрасывает ValueError при неверном формате.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {path} не найден")

    while lines and not lines[-1].strip():
        lines.pop()

    if not lines:
        raise ValueError("Файл пуст")

    header = lines[0].split()
    if len(header) != 2:
        raise ValueError("Неверный заголовок: ожидалось 2 числа")
    
    try:
        rows, cols = map(int, header)
    except ValueError:
        raise ValueError("Неверный заголовок: должны быть целые числа")

    if rows <= 0 or cols <= 0:
        raise ValueError("Размеры матрицы должны быть положительными")

    data_lines = lines[1:]
    if len(data_lines) != rows:
        raise ValueError(f"Ожидалось {rows} строк, найдено {len(data_lines)}")

    matrix = []
    for i, line in enumerate(data_lines, start=2):
        parts = line.split()
        if len(parts) != cols:
            raise ValueError(f"Строка {i}: ожидалось {cols} чисел, найдено {len(parts)}")
        
        try:
            row = [int(x) for x in parts]
        except ValueError:
            raise ValueError(f"Строка {i}: содержит нецелые числа")
        
        matrix.append(row)

    return matrix