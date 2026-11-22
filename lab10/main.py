# main.py
from pathlib import Path
from files_lab import read_matrix
from variant import selected_sum

def read_positive_integer():
    """Запрашивает целое число больше нуля."""
    while True:
        val = input("Введите положительное целое число: ")
        try:
            num = int(val)
            if num <= 0:
                print("Должно быть больше нуля")
            else:
                return num
        except ValueError:
            print("Не целое число")

def main():
    print("--- Проверка ввода ---")
    read_positive_integer()

    print("\n--- Обработка файла matrix.txt ---")
    file_path = Path(__file__).parent / "matrix.txt"
    
    try:
        matrix = read_matrix(file_path)
        print(f"Матрица прочитана успешно: {matrix}")

        # Считаем суммы строк и столбцов
        r_sums = [sum(row) for row in matrix]
        c_sums = [sum(col) for col in zip(*matrix)]
        
        # Считаем индивидуальный вариант
        var_sum = selected_sum(matrix)

        # Формируем отчет
        report_lines = [
            f"Суммы строк: {' '.join(map(str, r_sums))}",
            f"Суммы столбцов: {' '.join(map(str, c_sums))}",
            f"Результат варианта: {var_sum}"
        ]
        report_text = "\n".join(report_lines)

        # Записываем в файл
        report_path = Path(__file__).parent / "report.txt"
        report_path.write_text(report_text, encoding="utf-8")
        
        print("Отчет записан в report.txt")

    except FileNotFoundError:
        print("Ошибка: файл matrix.txt не найден.")
    except ValueError as e:
        print(f"Ошибка формата: {e}")
    except Exception as e:
        print(f"Ошибка доступа: {e}")

if __name__ == "__main__":
    main()