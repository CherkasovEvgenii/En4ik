# test_analysis.py
from analysis import validate_todos, completion_counts, top_users
from variant import select_tasks

def run_tests():
    data = [
        {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
        {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
        {"id": 3, "userId": 10, "title": "Строки", "completed": True},
        {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
        {"id": 5, "userId": 5, "title": "Списки", "completed": True}
    ]
    
    # Валидация
    validate_todos(data)
    
    # Подсчеты и лидеры
    counts = completion_counts(data)
    assert counts == {5: 2, 10: 2}
    assert top_users(counts) == [5, 10]
    
    # Тесты индивидуального варианта (id <= 2)
    assert select_tasks(data, 5, 2) == [1, 2]
    assert select_tasks(data, 99, 2) == [] # Неизвестный пользователь

    # Проверка на ошибку, если не передан параметр
    try:
        select_tasks(data, 5)
        assert False
    except ValueError:
        pass

    # Ошибка валидации (отрицательный id)
    try:
        validate_todos([{"id": -1, "userId": 1, "title": "A", "completed": True}])
        assert False
    except ValueError:
        pass

    print("Все тесты пройдены успешно!")

if __name__ == "__main__":
    run_tests()