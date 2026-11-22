# test_logic.py
from logic import add_record, find_records, set_completed, delete_record, statistics

def test_all():
    # Тест добавления
    records = []
    assert add_record(records, "Python", "Кодинг", 10) == 1
    assert add_record(records, "SQL", "Базы данных", 5) == 2
    assert len(records) == 2
    
    # Тест поиска
    assert len(find_records(records, "py")) == 1
    assert len(find_records(records, "НЕТ")) == 0
    
    # Тест изменения статуса
    assert set_completed(records, 1, True) is True
    assert records[0]["completed"] is True
    assert set_completed(records, 99, True) is False # Неизвестный ID
    
    # Тест статистики
    stats = statistics(records)
    assert stats["total"] == 2
    assert stats["completed"] == 1
    assert stats["not_completed"] == 1
    assert stats["total_amount"] == 15
    assert stats["by_category"] == {"Кодинг": 10, "Базы данных": 5}
    
    # Тест удаления
    assert delete_record(records, 1) is True
    assert len(records) == 1
    assert delete_record(records, 1) is False # Уже удалено
    
    print("Все тесты в test_logic.py пройдены!")

if __name__ == "__main__":
    test_all()