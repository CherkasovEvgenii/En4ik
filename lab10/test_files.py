# test_files.py
from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import read_matrix
from variant import selected_sum

def test_all():
    with TemporaryDirectory() as directory:
        path = Path(directory) / "matrix.txt"
        
        # Тесты чтения
        path.write_text("1 1\n0\n", encoding="utf-8")
        assert read_matrix(path) == [[0]]

        path.write_text("", encoding="utf-8")
        try:
            read_matrix(path)
            assert False
        except ValueError:
            pass

        path.write_text("0 3\n", encoding="utf-8")
        try:
            read_matrix(path)
            assert False
        except ValueError:
            pass

        path.write_text("1 2\n1\n", encoding="utf-8")
        try:
            read_matrix(path)
            assert False
        except ValueError as e:
            assert "Строка 2" in str(e)

        path.write_text("1 2\n1 x\n", encoding="utf-8")
        try:
            read_matrix(path)
            assert False
        except ValueError as e:
            assert "Строка 2" in str(e)

        path.write_text("1 1\n1\n2\n", encoding="utf-8")
        try:
            read_matrix(path)
            assert False
        except ValueError:
            pass

    # Тест индивидуального варианта 5
    test_matrix = [[1, -2, 3], [4, 0, -6]]
    # Кратные 3: 3, 0, -6. Сумма = -3.
    assert selected_sum(test_matrix) == -3
    assert selected_sum([[1, 2], [4, 5]]) == 0

    print("Все тесты пройдены успешно!")

if __name__ == "__main__":
    test_all()